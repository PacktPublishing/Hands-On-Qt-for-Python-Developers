# -*- coding: utf-8 -*-         #   PYTHON 3   #
from PyQt5 import QtWidgets, QtCore, QtGui     # Import of the PyQt5 modules.


class GRectItem(QtWidgets.QGraphicsRectItem):  # Graphics rectangle item.
    
    def __init__(self, parent=None, painter=None, w=500.0, h=500.0):
        super(GRectItem, self).__init__(parent)
        self.w = w                             # Width and height of the                            
        self.h = h                             # rectangle are required.
        self.setRect(0.0, 0.0, self.w, self.h)

    def paint(self, painter, *args):           # Method to paint on the item.
        painter = painter                      # Painter that will be used. 
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtCore.Qt.red)        # Brush with color for paint.
        painter.setPen(QtCore.Qt.green)        # Pen with color for paint.
        for dp in range(1, 100):               # Will call function to draw
            self.drawPoints(painter, dp)       # in the loop with range.
    
    def drawPoints(self, painter, dp):         # Function to draw the points.
        painter.drawPoint(self.w/2+dp, self.h/2+dp)
        painter.save()                         # Will save the paint state.

