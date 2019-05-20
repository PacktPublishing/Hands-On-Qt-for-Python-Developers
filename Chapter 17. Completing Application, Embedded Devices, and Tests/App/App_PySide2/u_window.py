# -*- coding: utf-8 -*-         #   PYTHON 2   #
from PySide2 import QtWidgets, QtCore, QtGui   # Import of PySide2 modules.
from u_style import UWin, UWid, UMBar, USBar, UMenu, UTWid


class UWindow(UWin):                           # Create the Main Window.
    
    def __init__(self, parent=None):           # Constructor of the class.
        super(UWindow, self).__init__(parent)  # Initialization of the class.
        self.menubar = UMBar()                 # Menu Bar for main window.
        self.mb1 = UMenu(self.menubar)         # First Menu for Menu Bar.
        self.mb1.addAction("Open")             # Menu, that will create,
        self.mb1.addAction("Save")             # open and save files and 
        self.mb1.addAction("Print")            # open print dialog with 
        self.mb1.addAction("Print Preview")    # open print preview dialog,
        self.mb1.setTitle("&File")             # used in the application.
        self.mb2 = UMenu(self.menubar)         # Second Menu for Menu Bar.
        self.mb2.addAction("Undo")             # Adding of the elements of
        self.mb2.addAction("Redo")             # the Menu that will edit 
        self.mb2.addAction("Cut")              # some documents created with
        self.mb2.addAction("Copy")             # this app, undoes and redoes
        self.mb2.addAction("Paste")            # operations, cut/copy/past
        self.mb2_1 = self.mb2.addMenu("&Alignment")
        self.mb2_1.addAction("center")         # for the text edit field.
        self.mb2_1.addAction("left")           # Adding of the submenu for 
        self.mb2_1.addAction("right")          # alignment of the text in the
        self.mb2_1.addAction("justify")        # text field by center, right,
        self.mb2.addAction("Text Color")       # left, and justified. Adding
        self.mb2.addAction("Text Font")        # options for change color and
        self.mb2.setTitle("&Edit")             # font for selected text.
        self.mb3 = UMenu(self.menubar)         # Third Menu for Menu Bar.
        self.mb3.addAction("Pickle")           # Add elements to provide 
        self.mb3.addAction("Shelve")           # open the data with pickle,
        self.mb3.addAction("CSV")              # shelve, csv, pandas, sqlite,
        self.mb3.addAction("Pandas")           # postgresql, mysql, qtsql
        self.mb3.addAction("SQLite")           # module operations, NoSQL  
        self.mb3.addAction("PostgreSQL")       # databases MongoDB, CouchDB.
        self.mb3.addAction("MySQL")            # Each option will open the 
        self.mb3.addAction("MongoDB")          # file/db with providing 
        self.mb3.addAction("CouchDB")          # functionality dependent on
        self.mb3.setTitle("&Data")             # selected option.          
        self.mb4 = UMenu(self.menubar)         # Fourth Menu for Menu Bar.
        self.mb4.addAction("Settings")         # Add elements to provide 
        self.mb4.addAction("Run")              # some settings, run and
        self.mb4.addAction("Configuration")    # configure some parameters
        self.mb4.setTitle("&Options")          # of the app as some options.
        self.mb5 = UMenu(self.menubar)         # Fifth Menu for Menu Bar.
        self.mb5.addAction("Online Help")      # Provides links to online
        self.mb5.addAction("Documentation")    # help and other docs that
        self.mb5.setTitle("&Help")             # will related to this app.
        self.menubar.addMenu(self.mb1)         # Add first menu to menu bar.
        self.menubar.addMenu(self.mb2)         # Add second menu to menu bar.
        self.menubar.addMenu(self.mb3)         # Add third menu to menu bar.
        self.menubar.addMenu(self.mb4)         # Add fourth menu to menu bar.
        self.menubar.addMenu(self.mb5)         # Add fifth menu to menu bar.
        self.setMenuBar(self.menubar)          # And set menu bar to window.
        self.tabwid = UTWid()                  # Tab Widget for main window.
        self.twid1 = UWid()                    # First widget for tab widget.
        self.twid2 = UWid()                    # Second widget for tabwidget.
        self.twid3 = UWid()                    # Third widget for tab widget.
        self.tabwid.addTab(self.twid1, "Applications")
        self.tabwid.addTab(self.twid2, "Visualization")
        self.tabwid.addTab(self.twid3, "Documents")
        self.setCentralWidget(self.tabwid)     # Central widget as tabwidget.
        self.stat_bar = USBar()                # Create status bar object.
        self.setStatusBar(self.stat_bar)       # Set status bar.
