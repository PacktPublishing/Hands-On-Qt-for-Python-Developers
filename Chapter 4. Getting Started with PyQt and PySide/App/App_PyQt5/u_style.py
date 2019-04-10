# -*- coding: utf-8 -*-         #   PYTHON 3   #
from PyQt5 import QtWidgets, QtCore, QtGui     # Import of the PyQt5 modules.

color = ["rgba(0,41,59,140)", "rgba(0,41,59,255)"]


class UWid(QtWidgets.QWidget):                 # Class for QWidget.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UWid, self).__init__(parent)     # widget initialization.
        self.setWindowTitle("U App")           # Title of the application.
        self.setStyleSheet("background-color: %s;" % (color[0],))
