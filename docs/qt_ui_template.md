# Basic Class for PySide2 UIs

```Python
import hou
from PySide2 import QtCore, QtUiTools, QtWidgets


class Classname(QtWidgets.QWidget):
    def __init__(self):
        super(Classname, self).__init__()
        ui_file = "PATH/TO/UI.ui"
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)


def run():
    win = Classname()
    win.show()
```


# Shelftool Script
```Python
import file_name

reload(file_name)
file_name.run()
```
