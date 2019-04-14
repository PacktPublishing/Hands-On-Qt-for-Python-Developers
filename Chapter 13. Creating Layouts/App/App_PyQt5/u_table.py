# -*- coding: utf-8 -*-         #   PYTHON 3   #
from PyQt5 import QtCore                       # Importing of the models.
import random                                  # Python stdlib module.


class UIModel(QtCore.QAbstractItemModel):      # Abstract class using to
    
    def __init__(self, parent=None):           # implementing the item model.
        super(UIModel, self).__init__(parent)  # Initialization of the class.

    def rowCount(self, parent):                # Required method that returns
        return 50                              # the total number of rows.

    def columnCount(self, parent):             # Required method that returns
        return 10                              # the total number of columns.
    
    def index(self, row, column, parent):      # Required method that returns
        return parent                          # the index of row/column.
    
    def data(self, index, role):               # Required method that returns
        return 1                               # the data for each cell.


class UTModel(QtCore.QAbstractTableModel):     # Class for the model.

    def __init__(self, parent=None):           # Constructor for this class.
        super(UTModel, self).__init__(parent)  # Initialization of the class.

    def rowCount(self, parent):                # Function that will return
        return 27                              # the total number of rows.

    def columnCount(self, parent):             # Function that will return
        return 14                              # the total number of columns.

    def data(self, row, column):               # Function that will return
        randn = random.randint(1, 100)         # the data for this model as
        return randn                           # random numbers for items.