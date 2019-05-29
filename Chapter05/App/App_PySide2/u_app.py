# -*- coding: utf-8 -*-         #   PYTHON 2   #
from u_tools import UTools                     # Importing of the functions.
from u_style import UWid                       # Import styled widget.
from u_window import UWindow                   # Importing the Main Window.


class UApp(UWindow, UTools):                   # Create the main class.
    
    def __init__(self, parent=None):           # Constructor of the class.
        super(UApp, self).__init__(parent)     # Initialization of the class.
        UTools.__init__(self)                  # Initialization of the
        # print self.us1                       # class with functions.


if __name__ == "__main__":                     # If file run, name will main.
    import sys                                 # Import sys from stdlib.
    from PySide2 import QtWidgets, QtCore, QtGui
    app = QtWidgets.QApplication(sys.argv)     # Create application.
    uap = UApp()                               # Main class instance
    uap.show()                                 # Show the widget when start.
    sys.exit(app.exec_())                      # Executes the application.
