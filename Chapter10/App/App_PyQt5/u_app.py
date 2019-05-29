# -*- coding: utf-8 -*-         #   PYTHON 3   #
from u_tools import UTools                     # Importing the functions.
from u_style import UWid, UFrame, ULabel       # Import the styled widgets.
from u_style import ULineEd, UTextEd           # Import the styled widgets.
from u_style import UComBox, UListV, UTabView  # Import the styled widgets.
from u_style import UBut1                      # Import the styled widgets.
from u_style import UProgress                  # Import the styled widgets.
from u_window import UWindow                   # Importing the Main Window.
from u_table import UTModel                    # Import of the table model.


class UApp(UWindow, UTools):                   # Create the main class.

    def __init__(self, parent=None):           # Constructor of the class.
        super(UApp, self).__init__(parent)     # Initialization of the class.
        UTools.__init__(self)                  # Initialization of the tools
        # print(self.us1)                      # class with functions.
        self.frame1 = UFrame(self.twid3)       # Create the first frame with
        self.frame1.setLineWidth(3)            # parent as third widget.
        self.frame1.setFrameStyle(6)           # Styled panel frame style.
        self.table = UTabView(self.frame1)     # Creation of the table with
        self.table.setVisible(False)           # parent as frame 1 and gets
        model = UTModel()                      # data from the model.
        self.table.setModel(model)             # Set model data to the table.
        self.text_edit = UTextEd(self.frame1)  # Text Edit field with
        self.layfr1 = QtWidgets.QGridLayout()  # parent - the first frame.
        self.layfr1.addWidget(self.table, 0, 0, 1, 1)
        self.layfr1.addWidget(self.text_edit, 0, 0, 1, 1)
        self.frame1.setLayout(self.layfr1)     # Layout for this field.
        self.frame2 = UFrame(self.twid3)       # Second with parent as 3d wid.
        self.frame2.setLineWidth(3)            # Sets line width of the frame
        self.frame2.setFrameStyle(0)           # and 0 - style NoFrame.
        self.frame2.setMaximumWidth(int(self.width()/3))
        self.label1 = ULabel(self.frame2)      # Label in the second frame.
        self.label1.setText("User Information")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.combox1 = UComBox(self.frame2)    # Add the combo box and items.
        self.combox1.addItems(["Texts", "Table"])
        self.combox1.setView(UListV())         # Combo box popup view.
        self.line_ed1 = ULineEd(self.frame2)   # First line edit field.
        self.line_ed1.setPlaceholderText("Full Name...")
        self.line_ed2 = ULineEd(self.frame2)   # Second for user email.
        self.line_ed2.setPlaceholderText("Email...")
        self.line_ed3 = ULineEd(self.frame2)   # Third field for input passw.
        self.line_ed3.setPlaceholderText("Password...")
        self.line_ed3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.push_but1 = UBut1(self.frame2)    # Adding the button with text.
        self.push_but1.setText("Ok")           # Adding progress bar with
        self.progress1 = UProgress(self.frame2)
        self.progress1.setRange(0, 0)          # range (indeterminate mode).
        self.layfr2_1 = QtWidgets.QGridLayout()
        self.layfr2_1.addWidget(self.push_but1, 0, 1, 1, 1)
        self.layfr2_1.addWidget(self.progress1, 1, 0, 1, 2)
        self.layfr2 = QtWidgets.QGridLayout()  # Layout for the second frame.
        self.layfr2.addWidget(self.combox1, 0, 0, 1, 1)
        self.layfr2.addWidget(self.label1, 1, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed1, 2, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed2, 3, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed3, 4, 0, 1, 1)
        self.layfr2.addLayout(self.layfr2_1, 5, 0, 1, 1)
        self.frame2.setLayout(self.layfr2)     # Layout added to frame.
        self.lay1 = QtWidgets.QGridLayout()    # Layout for the third widget.
        self.lay1.addWidget(self.frame1, 0, 0, 1, 1)
        self.lay1.addWidget(self.frame2, 0, 1, 1, 1)
        self.twid3.setLayout(self.lay1)        # Set layout to the widget.
        self.combox1.activated.connect(self.txt_table)

    def txt_table(self):                       # The function that will
        if self.combox1.currentText() == "Texts":
            self.text_edit.setVisible(True)    # visualize the table and text
            self.table.setVisible(False)       # depends on choice of combo.
        if self.combox1.currentText() == "Table": 
            self.text_edit.setVisible(False)   # When the text activated,
            self.table.setVisible(True)        # elements visible or not.


if __name__ == "__main__":                     # If file run, name will main.
    import sys                                 # Import sys from stdlib.
    from PyQt5 import QtWidgets, QtCore, QtGui
    app = QtWidgets.QApplication(sys.argv)     # Create application.
    uap = UApp()                               # Class instance.
    uap.show()                                 # Show the widget when start.
    sys.exit(app.exec_())                      # Executes the application.
