# -*- coding: utf-8 -*-         #   PYTHON 3   #
from PyQt5 import QtTest                       # Importing for the tests.
from PyQt5.QtWidgets import QApplication       # Importing for application.
from PyQt5.Qt import Qt                        # Import of the Qt namespaces.
from u_window import UWindow                   # Import the testing widget.
import unittest                                # Stdlib module for test.


class UTests(unittest.TestCase):               # Class realizes the tests.

    def setUp(self):                           # Function for setup before
        self.app = QApplication([])            # tests, creation of the app,
        self.uwin = UWindow()                  # window instances, menubar  
        self.menu = self.uwin.menuBar()        # for using in the test.

    def test_menu(self):                       # Function for test menu.
        self.assertEqual(self.uwin.mb1.title(), "&File")
        self.menu.actions()[0].trigger()       # Activation of the trigger.
        QtTest.QTest.keyPress(self.uwin, Qt.Key_Enter, Qt.ControlModifier)
        return                                 # Simulates enter key press.

    def tear_down(self):                       # Called after test has been
        pass                                   # called and result recorded. 


unittest.main()                                # Starts test with unittest.
