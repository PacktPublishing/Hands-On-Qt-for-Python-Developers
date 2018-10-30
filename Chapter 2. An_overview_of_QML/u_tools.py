# -*- coding: utf-8 -*-
from PyQt5.QtCore import QUrl                 # Import for QML url.
from PyQt5.QtQml import QQmlApplicationEngine # QML engine.


class UTools():                               

    def __init__(self):
        self.us1 = "Application with Python."

    def u_qml(self, parent=None):             # Function to run QML`s
        self.qwid = QQmlApplicationEngine()   # with QtQml engine
        self.qwid.load(QUrl('u_qml.qml'))     # infrastructure.


if __name__ == "__main__":
    ut = UTools()
