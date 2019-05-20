# -*- coding: utf-8 -*-         #   PYTHON 2   #
from PySide2 import QtWidgets, QtCore          # Importing for app, url.
from PySide2.QtQml import QQmlApplicationEngine 
import sys                                     # The sys module for the app.

app = QtWidgets.QApplication(sys.argv)         # Creating application.
qwid = QQmlApplicationEngine()                 # QML app engine instance.
qwid.load(QtCore.QUrl('u_qml.qml'))            # Loads the QML file with URL.
sys.exit(app.exec_())                          # Executes the application.
