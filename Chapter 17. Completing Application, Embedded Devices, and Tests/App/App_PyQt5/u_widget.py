# -*- coding: utf-8 -*-         #   PYTHON 3   #
from PyQt5 import QtWidgets                    # Importing for grid layout.
from u_style import UWid, UTextEd, UComBox, UListV
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings


class UWidget(UWid):                           # Class for simple widget

    def __init__(self, parent=None):           # that can be used in the
        super(UWidget, self).__init__(parent)  # varios tasks. Inherits
        self.setWindowOpacity(0.95)            # custom styled UWid class.
        self.wview = QWebEngineView(self)      # Web implementation in the
        self.wview.settings().setAttribute(    # application. This class is
                QWebEngineSettings.PluginsEnabled, True)
        self.wview.settings().setAttribute(    # used to load web content
                QWebEngineSettings.AutoLoadImages, True)
        self.wview.settings().setAttribute(    # and functionality. The
                QWebEngineSettings.JavascriptEnabled, True)
        self.wview.setVisible(False)           # settings are provided.
        self.infotxt = UTextEd(self)           # Contains Text edit field,
        self.infocomb = UComBox(self)          # combobox for an option 
        self.infocomb.setView(UListV())        # selection. Widget window 
        self.infolay = QtWidgets.QGridLayout() # opacity if widget will
        self.infolay.addWidget(self.wview, 0, 0, 1, 1)
        self.infolay.addWidget(self.infotxt, 0, 0, 1, 1)
        self.infolay.addWidget(self.infocomb, 1, 0, 1, 1)
        self.infolay.setSpacing(0)             # be used without styling.
        self.infolay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.infolay)           # Layout arranging items.
