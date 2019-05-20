# -*- coding: utf-8 -*-         #   PYTHON 2   #
from PySide2 import QtWidgets, QtCore, QtGui   # Importing the PySide2. 


class ULayout(QtWidgets.QLayout):              # Reimplementing the layout.

    def __init__(self, parent=None):           # Constructor of the ULayout.
        super(ULayout, self).__init__(parent)  # Initialization of the class.
        self.setSpacing(10)                    # Sets spacing for layout.
        print self.getContentsMargins()        # Prints content margins.


class ULayoutItem(QtWidgets.QLayoutItem):      # Reimplementing the layout

    def __init__(self, parent=None):           # item for using in the app.
        super(ULayoutItem, self).__init__(parent)