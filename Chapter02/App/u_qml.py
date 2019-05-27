# -*- coding: utf-8 -*-
from PyQt5.QtCore import QUrl                      # Importing for using url.
from PyQt5.QtQml import QQmlApplicationEngine      # Import QML app engine.
from PyQt5 import QtWidgets                        # Import for application.


class UQml(QtWidgets.QWidget):                     # Class realizes the QML.

    def __init__(self, parent=None):               # This class can be used
        QtWidgets.QWidget.__init__(self, parent)   # to display the QMLs.
        self.start_qml()                           # Start the function.

    def start_qml(self):                           # Function use QML app
        self.qwid = QQmlApplicationEngine()        # engine to display
        self.qwid.load(QUrl('u_qml.qml'))          # the created QML apps.


if __name__ == "__main__":                         # If running as file, the
    import sys                                     # application window will
    app = QtWidgets.QApplication(sys.argv)         # be displayed with run
    qwin = UQml()                                  # of the QML independent
    # qwin.show()                                  # from another used apps
    sys.exit(app.exec_())                          # and widgets.
