import hou
from PySide2 import QtCore, QtUiTools, QtWidgets
import random

class GeoCreator(QtWidgets.QWidget):

    def checkSelection(self):
        try:
            self.selectedNode = hou.selectedNodes()[0]
            return(self.selectedNode)
            #TODO notice if more than one node selected
            
        except IndexError:
            print("no node selected")
            #TODO replace with error message
    
    def findallRamps(self,selectedNode):
        rampparms = []
    
        #iterate through all parms and find all ramp parms
        for parm in selectedNode.parms():
            if "Ramp" in str(parm.parmTemplate().type()):
                rampparms.append(parm.name())
    
        return(rampparms)
        
    def updateParmCombo(self):
        #TODO fix error if window is created with nothing selected
        #other functions continue even if checkSelection excepts
        selectedNode = self.checkSelection()
        parm_list = self.findallRamps(selectedNode)
        self.ui.parm_combo.clear()
        self.ui.parm_combo.addItems(parm_list)

    def overrideRandomRamp(self):
        #init values
        self.ptspos = []
        self.ptsvalue = []
        self.numpts = 10 #get from ui
        self.type = hou.rampBasis.Constant #get from ui
        self.rand_min = self.ui.over_fitlower_text.value()
        self.rand_max = self.ui.over_fitupper_text.value()
        self.ramp_node = self.selectedNode
        self.ramp_name = self.ui.parm_combo.currentText()

        #evenly split range and create random values
        for i in range(self.numpts + 1):
            self.currentpos = i * 1.0 / self.numpts
            self.ptspos.append(self.currentpos)
            self.currentvalue = random.uniform(self.rand_min, self.rand_max)
            self.ptsvalue.append(self.currentvalue)
    
            #convert list to tuples for hou.Ramp
            self.potspos = tuple(self.ptspos)
            self.ptsvalue = tuple(self.ptsvalue)
    
            #apply random values
            self.newramp = hou.Ramp((self.type,self.type),self.ptspos,self.ptsvalue)
            self.ramp_node.setParms({self.ramp_name: self.newramp})


    def adjustRandomRamp(self):
        pass

    def switchRandom(self):
        if self.ui.adjust_rbtn.isChecked():
            self.adjustRandomRamp()
            
        elif self.ui.override_rbtn.isChecked():
            self.overrideRandomRamp()
            
        else:
            pass

    def __init__(self):
        super(GeoCreator,self).__init__()
        ui_file = "D:/Projects/LEO_DEV/uiTutorial1/leo_randomRamp.ui"
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)
        
        # update parm combobox
        self.updateParmCombo()
        
        # button update selection
        self.ui.update_btn.clicked.connect(self.updateParmCombo)

        #button apply
        self.ui.apply_btn.clicked.connect(self.switchRandom)
        
win = GeoCreator()
win.show()