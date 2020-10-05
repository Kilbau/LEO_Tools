import hou
from PySide2 import QtCore, QtUiTools, QtWidgets


class GenerateHelp(QtWidgets.QWidget):
    def __init__(self):
        super(GenerateHelp, self).__init__()
        ui_file = hou.getenv("LEO") + "/scripts/python/leo_generate_help.ui"
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)

        # init values
        self.node = None

        self.node_title = None
        self.node_icon_path = None
        self.node_type = None
        self.node_context = None
        self.node_namespace = None
        self.node_internal_name = None
        self.node_version = None

        self.output_text = None

        def get_selected_node(self):
            self.node = hou.selectedNodes()[0]

        def get_values_from_node(self, version=0):
            """
            gets values from the current node
            version switches between two methods of getting the current hda version
            """
            node_info = self.node.type()
            name_components = node_info.nameComponents()

            self.node_title = node_info.description()
            self.node_icon_path = node_info.icon()
            self.node_type = "node"
            self.node_context = node_info.category().name().lower()

            self.node_namespace = name_components[1]
            self.node_internal_name = name_components[2]

            if version == 0:
                # from Assetname
                self.node_version = name_components[3]
            else:
                # from Basis - Version
                self.node_version = self.node.userDataDict().get("___Version___")

        def get_parameter_values_from_node(self, skip_hidden=0):
            """
            gets values from the parameters
            if skip_hidden hidden parameters will not be checked
            """

            # TODO: check if parm has a menu and then also create subcategories for each menuitem

            for parm in self.node.parms():
                parm_template = parm.parmTemplate

                parm_hidden = parm_template.isHidden()

                if parm_hidden and skip_hidden:
                    continue
                else:
                    parm_label = parm_template.label()
                    parm_name = parm_template.name()
                    parm_description = parm_template.help()
                    # TODO

        def get_input_values_from_node(self):
            """
            gets the names of the inputs and outputs of the hda
            """
            input_labels = self.node.input_labels()
            output_labels = self.node.output_labels()
            # TODO

        def create_help(self):
            """
            creates the output text and saves it as self.output_text
            input is a list of operations
            the list contains dictonaries with specific information based of the ui
            """


def run():
    win = GenerateHelp()
    win.show()
