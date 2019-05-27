# -*- coding: utf-8 -*-         #   PYTHON 3   #
from PyQt5 import QtWidgets, QtCore, QtGui     # Import of the PyQt5 modules.

color = ["rgba(0,41,59,140)", "rgba(0,41,59,255)",
         "rgba(1,255,217,140)", "rgba(1,255,217,255)"]


class UWin(QtWidgets.QMainWindow):             # Class for Main Window.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UWin, self).__init__(parent)     # initialization.
        self.setWindowTitle("U App")           # Title of the application.
        win_icon = QtGui.QIcon("Icons/python1.png")
        self.setWindowIcon(win_icon)           # Set icon.
        self.setWindowOpacity(0.95)            # Set widget opacity.
        self.setAnimated(True)                 # Set enabled.
        self.setAcceptDrops(True)              # Accept drop event.
        self.setMouseTracking(True)            # Mouse tracking enabled.
        self.setUpdatesEnabled(True)           # Updates enabled.
        self.setAutoFillBackground(True)       # Auto fill of background.
        self.setStyleSheet("background-color: %s;" % (color[0],))


class UMBar(QtWidgets.QMenuBar):               # Class for Menu Bar.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UMBar, self).__init__(parent)    # initialization the menubar.
        self.setStyleSheet("background-color: %s;" % (color[2],))


class UMenu(QtWidgets.QMenu):                  # Class for Menu.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UMenu, self).__init__(parent)    # initialization of the menu.
        self.setStyleSheet("background-color: %s;" % (color[2],))


class UTWid(QtWidgets.QTabWidget):             # Class for Tab Widget.

    def __init__(self, parent=None, twbdr=3, twbdw=0.5, twbbg=color[1],
                 tbpad=7, tbsize=140, tbbg=color[0], tbc=color[2],
                 tbcs=color[3]):               # Constructor with parameters.
        super(UTWid, self).__init__(parent)    # initialization of tabwidget.
        self.font1 = QtGui.QFont()             # Font for tab widget. 
        self.font1.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 2.0)
        self.font1.setWordSpacing(2.0)         # Set spacing between letters
        self.font1.setFamily("Verdana")        # and words, sets font family,
        self.font1.setPixelSize(12)            # sets font size in the pixels
        self.font1.setWeight(34)               # and font weight of the text.
        self.setFont(self.font1)               # Set font to the tab widget.
        self.twbdr = twbdr                     # Set parameters of the
        self.twbdw = twbdw                     # function of the class,
        self.twbbg = twbbg                     # that will be used in the
        self.tbsize = tbsize                   # functions of this class to
        self.tbpad = tbpad                     # styling. Parameters of the 
        self.tbbg = tbbg                       # borders size, background
        self.tbc = tbc                         # colors, text colors, size of
        self.tbcs = tbcs                       # the tabs in the tab bar.
        self.setStyleSheet(                    # Parameters with StyleSheet. 
                """QTabWidget::pane {border-style: solid; border-radius: %spx;
                    border-width: %spx; border-color: %s;}
                   QTabBar::tab {width: %spx; margin: 0px; padding: %spx;
                    background-color: %s; color: %s; border-style: solid;
                    border-top-right-radius: 10px; border-width: %spx;
                    border-bottom-width: 0px; border-color: %s;}
                   QTabBar::tab:selected {background-color: %s; color: %s;}
                   QTabBar::tab:!selected {margin-top: 5px;}
                   QTabBar QToolButton {color: %s;}"""
                   % (self.twbdr, self.twbdw, self.twbbg, self.tbsize,
                      self.tbpad, self.tbbg, self.tbc, self.twbdw, self.tbbg,
                      self.twbbg, self.tbcs, self.tbcs))


class USBar(QtWidgets.QStatusBar):             # Class for Status Bar.

    def __init__(self, parent=None):           # Constructor of the class and
        super(USBar, self).__init__(parent)    # initialization of bar.
        self.setStyleSheet("background-color: %s;" % (color[2],))


class UWid(QtWidgets.QWidget):                 # Class for Widget.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UWid, self).__init__(parent)     # initialization.
        self.setWindowTitle("U App")           # Title of the widget.
        win_icon = QtGui.QIcon("Icons/python1.png")
        self.setWindowIcon(win_icon)           # Set icon.
        self.setWindowOpacity(0.95)            # Set widget opacity.
        self.setAcceptDrops(True)              # Accept drop event.
        self.setMouseTracking(True)            # Mouse tracking enabled.
        self.setUpdatesEnabled(True)           # Updates enabled.
        self.setAutoFillBackground(True)       # Auto fill of the background.
        self.setStyleSheet("background-color: %s;" % (color[0],))
