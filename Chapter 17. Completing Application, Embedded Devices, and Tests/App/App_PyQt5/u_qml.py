# -*- coding: utf-8 -*-         #   PYTHON 3   #
from PyQt5 import QtWidgets, QtCore            # Importing for app, url.
from PyQt5.QtQml import QQmlApplicationEngine  # Importing the QML engine.
import sys                                     # The sys module for the app.

app = QtWidgets.QApplication(sys.argv)         # Creating application.
qwid = QQmlApplicationEngine()                 # QML app engine instance.
qwid.load(QtCore.QUrl('u_qml.qml'))            # Loads the QML file with URL.
sys.exit(app.exec_())                          # Executes the application.
