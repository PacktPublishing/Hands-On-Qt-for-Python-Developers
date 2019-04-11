# -*- coding: utf-8 -*-         #   PYTHON 2   #
from u_tools import UTools                     # Importing the Utools class.
from u_style import UWid, UFrame, ULabel       # Importing styled widgets.
from u_style import ULineEd, UTextEd           # Importing styled widgets.
from u_window import UWindow                   # Importing the Main Window.
import enchant                                 # Importing the package.
from u_adds import UHighLight                  # Text highlighting.


class UApp(UWindow, UTools):                   # Create the main class.
    
    def __init__(self, parent=None):           # Constructor of the class.
        super(UApp, self).__init__(parent)     # Initialization of the class.
        UTools.__init__(self)                  # Initialisation of the class
        print self.us1                         # with functions and string.
        self.frame1 = UFrame(self.twid3)       # Create the first frame with
        self.frame1.setLineWidth(3)            # parent as third widget.
        self.frame1.setFrameStyle(6)           # Styled panel frame style.
        self.text_edit = UTextEd(self.frame1)  # Text Edit field with 
        self.layfr1 = QtWidgets.QGridLayout()  # parent - the first frame.
        self.layfr1.addWidget(self.text_edit, 0, 0, 1, 1)
        self.frame1.setLayout(self.layfr1)     # Layout for this field.
        self.frame2 = UFrame(self.twid3)       # Second frame with parent.
        self.frame2.setLineWidth(3)            # Sets line width of the frame
        self.frame2.setFrameStyle(0)           # and 0 - style NoFrame.
        self.frame2.setMaximumWidth(int(self.width()/3))
        self.label1 = ULabel(self.frame2)      # Label will be in the second
        self.label1.setText("User Information")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.line_ed1 = ULineEd(self.frame2)   # First line edit.
        self.line_ed1.setPlaceholderText("Full Name...")
        self.line_ed2 = ULineEd(self.frame2)   # Second for user email.
        self.line_ed2.setPlaceholderText("Email...")
        self.line_ed3 = ULineEd(self.frame2)   # Third field for input passw.
        self.line_ed3.setPlaceholderText("Password...")
        self.line_ed3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.layfr2 = QtWidgets.QGridLayout()  # Adding to the layout.
        self.layfr2.addWidget(self.label1, 0, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed1, 1, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed2, 2, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed3, 3, 0, 1, 1)
        self.frame2.setLayout(self.layfr2)     # Sets layout to the frame.
        self.lay1 = QtWidgets.QGridLayout()    # Layout for third widget.
        self.lay1.addWidget(self.frame1, 0, 0, 1, 1)
        self.lay1.addWidget(self.frame2, 0, 1, 1, 1)
        self.twid3.setLayout(self.lay1)        # Will be represented by grid.
        self.dicts = enchant.Dict("en_US")     # Set the dictionary.
        self.highlighter = UHighLight(self.text_edit.document())
        self.highlighter.setDict(self.dicts)   # set dict to highlighter.
        

if __name__ == "__main__":                     # If file will run, will main.
    import sys                                 # Import sys from stdlib.
    from PySide2 import QtWidgets, QtCore, QtGui
    app = QtWidgets.QApplication(sys.argv)     # Creates application.
    uap = UApp()                               # Class instance of the app.
    uap.show()                                 # Show the widget when start.
    sys.exit(app.exec_())                      # Executes the application.
