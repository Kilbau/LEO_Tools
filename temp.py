"""
State:          LEO::colorRampPicker::1
State type:     LEO::colorRampPicker::1
Description:    LEO::colorRampPicker::1
Author:         Kilian
Date Created:   June 01, 2020 - 17:34:50
"""


import hou
import viewerstate.utils as su

class State(object):
    MSG = "Click and hold the LMB to sample colors from an image"

    def __init__(self, state_name, scene_viewer):
        self.state_name = state_name
        self.scene_viewer = scene_viewer

        self.pressed = False
        self.index = 0    
        self.node = None

        self.imageSwitchNode = None

        self.imageGeometry = None

        self.interpolation = hou.rampBasis.Linear #sets the ramp interpolation
        self.rampParm = None

        self.colorList = []

        self.mouseState = 0 #responsible that only the lmb triggers the hou.uiEventReason.Changed event and not mmb or rmb


    def onEnter(self, kwargs):
        with hou.undos.disabler():
            self.node = kwargs["node"]

            self.imageSwitchNode = self.node.node("IMAGE_REFERENCE")
            self.imageSwitchNode.setParms({"input":1})

            self.imageGeometry = self.node.node("IMAGE").geometry()
            self.node.node("normal1").cook(force=True) #force cook to fix black normals

            self.rampParm = self.node.parm("ramp")

            if not self.node:
                raise

            self.scene_viewer.setPromptMessage( State.MSG )

    def onInterrupt(self,kwargs):
        with hou.undos.disabler():
            self.imageSwitchNode.setParms({"input":0})
            self.node.parm("points").set(0)


    def onResume(self, kwargs):
        with hou.undos.disabler():
            self.scene_viewer.setPromptMessage( State.MSG )
            self.imageSwitchNode.setParms({"input":1})

            self.node.node("normal1").cook(force=True) #force cook to fix black normals

    def onMouseEvent(self, kwargs):
        """ get the color undor the cursor if the lmb is pressed
        """
        ui_event = kwargs["ui_event"]
        device = ui_event.device()
        reason = ui_event.reason()                      

        # LMB functionality: pick colors from image
        if device.isLeftButton():
            with hou.undos.disabler():
                if reason == hou.uiEventReason.Start:

                    # reset self.colorList
                    self.colorList = []

                    #reset guide points
                    self.node.parm("points").set(0)

                    #set mouseState for uiEventReason.Changed
                    self.mouseState = 1

                if reason == hou.uiEventReason.Active:
                    # check for intersection with image
                    origin, direction = ui_event.ray()
                    hit, pos, norm, uvw = su.sopGeometryIntersection(self.imageGeometry, origin, direction)

                    if hit > -1:
                        # get color value under cursor
                        u, v, w = uvw
                        hitprim = self.imageGeometry.prim(hit)
                        hitcolor = hitprim.attribValueAtInterior("Cd", u, v, w)

                        # add color value to self.colorList
                        self.colorList.append(hitcolor)

                        # increment guide points and set postion
                        self.incrementGuidePoints(kwargs, pos)

        # funcionality runs after each lmb action 
        if reason == hou.uiEventReason.Changed and self.mouseState == 1:
            with hou.undos.disabler():
                self.node.parm("points").set(0)

            with hou.undos.group("LEO Picking Colors"):
                self.updateRamp(kwargs)
                self.mouseState = 0
       
        return True

    def onExit(self,kwargs):
        """ Called when the state terminates
        """
        with hou.undos.disabler():
            state_parms = kwargs["state_parms"]
            self.imageSwitchNode.setParms({"input":0})
            self.node.parm("points").set(0)

    def onDraw( self, kwargs ):
        """ move the image to the current viewport cam postion
        """
        with hou.undos.disabler():
            #copied from labs trimtexture
            viewport = hou.ui.curDesktop().paneTabOfType(hou.paneTabType.SceneViewer).curViewport()
            cam = viewport.viewTransform()

            #extract transforms
            rotation = cam.extractRotates()
            translation = cam.extractTranslates()

            #update hda parms
            node = kwargs["node"]
            node.parmTuple("vCamTranslate").set(tuple(translation))
            node.parmTuple("vCamRotate").set(tuple(rotation))
        
    def updateRamp(self, kwargs):
        """ create a houdini ramp and set the ramp parameter in the node
        """
        valuelist = []
        colorcount = len(self.colorList)

        for i in range(colorcount):
            try:
                value = float(i) / (colorcount-1)
            except ZeroDivisionError:
                #this catches the event where only one point is sampled
                value = 0
            finally:
                valuelist.append(value)

        new_ramp = hou.Ramp((self.interpolation, self.interpolation), tuple(valuelist), tuple(self.colorList))
        self.rampParm.set(new_ramp)   

    def incrementGuidePoints(self,kwargs,pos):
        """ increments the number of guide points
        """
        with hou.undos.disabler():
            # get number of points
            numpoints = self.node.parm("points").eval()

            # increment number of points
            numpoints += 1
            self.node.parm("points").set(numpoints)

            # enable points and set position
            ptnum = int(numpoints - 1)
            self.node.parmTuple("pt%d" % ptnum).set(pos)

def createViewerStateTemplate():
    """ Mandatory entry point to create and return the viewer state 
        template to register. """

    state_typename = kwargs["type"].definition().sections()["DefaultState"].contents()
    state_label = "LEO::colorRampPicker::1"
    state_cat = hou.sopNodeTypeCategory()

    template = hou.ViewerStateTemplate(state_typename, state_label, state_cat)
    template.bindFactory(State)
    template.bindIcon(kwargs["type"].icon())

    return template
