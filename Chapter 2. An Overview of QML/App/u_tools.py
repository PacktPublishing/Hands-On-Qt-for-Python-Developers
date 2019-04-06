# -*- coding: utf-8 -*-
from PyQt5.QtCore import QUrl                  # Importing for using url.
from PyQt5.QtQml import QQmlApplicationEngine  # Import QML app engine.

                                             
class UTools():                                # Class used with UApp class. 

    def __init__(self):                        # Constructor of the class
        self.us1 = "QML with Python."          # with informative string.

    def u_qml(self):                           # Function displays QML app.
        self.qwid = QQmlApplicationEngine()    # Create application engine.
        self.qwid.load(QUrl('u_qml.qml'))      # Load URL of the QML file.


if __name__ == "__main__":                     # If will be started as file
    ut = UTools()                              # class instance will be used.
