# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets                  # Will be used in the future.
from u_tools import UTools                   # Importing of the UTools class.


class UApp(QtWidgets.QWidget, UTools):       # Inheritance of the UTools.

    def __init__(self, parent=None):         # Constructor of the class.
        QtWidgets.QWidget.__init__(self, parent)
        UTools.__init__(self)                # Initialization of the UTools.
        self.start_qml()                     # Run the function start_qml.

    def start_qml(self):                     # Function to start QML.
        self.u_qml()                         # Function from UTools class.


if __name__ == "__main__":                   # If will be running as file.
    import sys                               # sys standard library module.
    app = QtWidgets.QApplication(sys.argv)   # Creates the GUI application.
    uap = UApp()                             # Instance of the UApp class.
    # uap.show()                             # Show application widget.
    sys.exit(app.exec_())                    # Execution of the application.
