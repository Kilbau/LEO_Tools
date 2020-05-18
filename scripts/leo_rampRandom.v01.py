import hou
from PySide2 import QtCore, QtUiTools, QtWidgets

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

    def __init__(self):
        super(GeoCreator,self).__init__()
        ui_file = "D:/Projects/LEO_DEV/uiTutorial1/leo_randomRamp.ui"
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)
        
        # update parm combobox
        self.updateParmCombo()
        
        # button update selection
        self.ui.update_btn.clicked.connect(self.updateParmCombo)
        
win = GeoCreator()
win.show()