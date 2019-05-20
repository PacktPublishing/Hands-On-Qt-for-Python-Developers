# -*- coding: utf-8 -*-         #   PYTHON 2   #
from PySide2 import QtWidgets, QtCore, QtGui   # Importing PySide2 modules.
from u_style import ULineEd, UBut1             # Importing field and button.


class USets(QtWidgets.QWidget):                # Class for settings.

    def __init__(self, parent=None):           # Constructor of the class and
        super(USets, self).__init__(parent)    # initialization.
        self.setWindowTitle("U App settings")  # Title of this widget.
        win_icon = QtGui.QIcon("Icons/python1.png")
        color_icon = QtGui.QIcon("Icons/colors.png")
        self.setWindowIcon(win_icon)           # Set widget window icon.
        rstop = open("settings.txt", "r")      # Open file with colors.
        rstyle = rstop.read().split(" ")       # Read and split by space.
        rstop.close()                          # Close settings file.
        self.bgle1 = ULineEd(self, tmrgl=30, tmrgt=20, tmrgr=0, tmrgb=20)
        self.bgle1.setText(rstyle[0])          # Field for background color.
        self.bgle1.setMinimumWidth(270)        # Minimum width for line edit.
        self.bgb1 = UBut1(self.bgle1, pad=1)   # Button to choose color.
        self.bgb1.setIcon(color_icon)          # Sets icon for button.
        self.bgle2 = ULineEd(self, tmrgl=30, tmrgt=20, tmrgr=0, tmrgb=20)
        self.bgle2.setText(rstyle[1])          # Field for background color.
        self.bgb2 = UBut1(self.bgle2, pad=1)   # Second button, the parents
        self.bgb2.setIcon(color_icon)          # of all buttons - fields.
        self.colle1 = ULineEd(self, tmrgl=30, tmrgt=20, tmrgr=0, tmrgb=20)
        self.colle1.setText(rstyle[2])         # Field for text color, other.
        self.colb1 = UBut1(self.colle1, pad=1)
        self.colb1.setIcon(color_icon)         # Third button, open dialog.
        self.colle2 = ULineEd(self, tmrgl=30, tmrgt=20, tmrgr=0, tmrgb=20)
        self.colle2.setText(rstyle[3])         # Field for text color, other.
        self.colb2 = UBut1(self.colle2, pad=1)
        self.colb2.setIcon(color_icon)         # The 1 and 2 bg colors
        self.lbinfo = QtWidgets.QLabel(self)   # recommended to be different.
        self.lbinfo.setText("""These settings will be saved and\n
                            application will be restarted""")
        self.breset = UBut1(self, fixw=95, fixh=59)
        self.breset.setText("Reset")           # Button to reset settings.
        self.bsave = UBut1(self, fixw=95, fixh=59)
        self.bsave.setText("Save")             # Button to save settings.
        hlay = QtWidgets.QHBoxLayout()         # Horizontal box layout for
        hlay.addWidget(self.lbinfo)            # button to delete the file
        hlay.addWidget(self.breset)            # and to save colors to the
        hlay.addWidget(self.bsave)             # file and label with text. 
        form_layout = QtWidgets.QFormLayout()  # Form layout with rows.
        form_layout.addRow("Background color 1", self.bgle1)
        form_layout.addRow("Background color 2", self.bgle2)
        form_layout.addRow("Color 1", self.colle1)
        form_layout.addRow("Color 2", self.colle2)
        vlay = QtWidgets.QVBoxLayout()         # Vertical box layout where
        vlay.addLayout(form_layout)            # will be Form layout and 
        vlay.addLayout(hlay)                   # horizontal box layout.
        self.setLayout(vlay)                   # Set vertical to widget.
        self.bgb1.clicked.connect(self.b1_fd)  # Signals that connects the 
        self.bgb2.clicked.connect(self.b2_fd)  # color buttons to functions. 
        self.colb1.clicked.connect(self.b3_fd)
        self.colb2.clicked.connect(self.b4_fd)

    def b1_fd(self):                           # First color dialog function
        self.color_fd(le=self.bgle1)           # with first line edit field.

    def b2_fd(self):                           # Second color dialog function
        self.color_fd(le=self.bgle2)           # with second line edit field.

    def b3_fd(self):                           # Third color dialog function
        self.color_fd(le=self.colle1)          # with third line edit field.

    def b4_fd(self):                           # Fourth color dialog function
        self.color_fd(le=self.colle2)          # with fourth line edit field.
    
    def color_fd(self, le=None):               # Function to run color dialog
        fd = QtWidgets.QColorDialog()          # with functions above. If the
        fd.setWindowIcon(QtGui.QIcon("Icons/python1.png"))
        if fd.exec_() == QtWidgets.QDialog.Accepted:
            fc = fd.selectedColor()            # dialog is accepted returns
            color = "rgba(%s,%s,%s,%s)" % (fc.red(), fc.green(), 
                          fc.blue(), fc.alpha())
            le.setText(color)                  # color, adds string to field.


if __name__ == "__main__":                     # If file run, name is main.
    import sys                                 # Import sys python stdlib.
    sapp = QtWidgets.QApplication(sys.argv)    # Create application.
    uset = USets()                             # Main class instance.
    uset.show()                                # Show the widget when start.
    sys.exit(sapp.exec_())                     # Executes the application.