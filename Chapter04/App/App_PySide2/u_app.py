# -*- coding: utf-8 -*-         #   PYTHON 2   #
from u_tools import UTools                     # Importing UTools class.
from u_style import UWid                       # Importing the styled widget.


class UApp(UWid, UTools):                      # Main class of the app.
    
    def __init__(self, parent=None):           # Constructor of the class.
        super(UApp, self).__init__(parent)     # Initialization of the class.
        UTools.__init__(self)                  # Initialization of the
        print self.us1                         # class with functions.


if __name__ == "__main__":                     # Run as file, name is main.
    import sys                                 # sys module - python stdlib.
    from PySide2 import QtWidgets, QtCore, QtGui
    app = QtWidgets.QApplication(sys.argv)     # Creating the application.
    uap = UApp()                               # Class instance.
    uap.show()                                 # Show the widget.
    print "sys module list of arguments: ", sys.argv
    print "      qApp list of arguments: ", QtWidgets.qApp.arguments()
    print "      Application Process ID: ", QtWidgets.qApp.applicationPid()
    print "        Application instance: ", QtWidgets.qApp.instance()
    print "           Application state: ", QtWidgets.qApp.applicationState()
    print "        Application platform: ", QtWidgets.qApp.platformName()
    for wi in QtWidgets.qApp.allWidgets():     # All widgets used with app.
        print "                      widget: ", wi
    sys.exit(app.exec_())                      # Executes the application.
