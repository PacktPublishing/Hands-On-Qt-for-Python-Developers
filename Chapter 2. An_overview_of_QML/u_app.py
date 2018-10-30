# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets             # Will be used in the futue.
from u_tools import UTools              # Import UTools class.


class UApp(QtWidgets.QWidget, UTools):  # Inheritance of the QWidget
                                        # and UTools class.
    def __init__(self, parent=None):    # Constructor of the UApp class.
        QtWidgets.QWidget.__init__(self, parent)  # Initialization of
        UTools.__init__(self)                     # the constructors.
        self.start_qml()                # Run function that start QML.

    def start_qml(self):                # Function to start QML with
        self.u_qml()                    # python.


if __name__ == "__main__":              # If name is not main is imported.
    import sys                          # Standard library module              
    app = QtWidgets.QApplication(sys.argv)    # Create the app.
    uap = UApp()                              # Class instance.
    # uap.show()                        # show application widget
    sys.exit(app.exec_())               # Application execution.
