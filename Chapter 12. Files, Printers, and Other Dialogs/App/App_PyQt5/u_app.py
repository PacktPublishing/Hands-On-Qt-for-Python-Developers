# -*- coding: utf-8 -*-         #   PYTHON 3   #
from u_tools import UTools                     # Importing of the functions.
from u_style import UWid, UFrame, ULabel       # Import the styled widgets.
from u_style import ULineEd, UTextEd           # Import the styled widgets.
from u_style import UComBox, UListV, UTabView  # Import the styled widgets.
from u_style import UBut1                      # Import the styled widgets.
from u_style import UProgress                  # Import the styled widgets.
from u_window import UWindow                   # Importing the Main Window.
from u_table import UTModel                    # Import of the table model.
from PyQt5 import QtPrintSupport               # Importing for printing.


class UApp(UWindow, UTools):                   # Create the main class.

    def __init__(self, parent=None):           # Constructor of the class.
        super(UApp, self).__init__(parent)     # Initialization of the class.
        UTools.__init__(self)                  # Initialization of the tools
        print(self.us1)                        # class with functions.
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
        self.frame1.setLayout(self.layfr1)     # layout for this field.
        self.frame2 = UFrame(self.twid3)       # Second frame with parent.
        self.frame2.setLineWidth(3)            # Sets line width of the frame
        self.frame2.setFrameStyle(0)           # and 0 - style No frame.
        self.frame2.setMaximumWidth(int(self.width()/3))
        self.label1 = ULabel(self.frame2)      # Label in the second frame.
        self.label1.setText("User Information")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.combox1 = UComBox(self.frame2)    # Adding the combo box.
        self.combox1.addItems(["Texts", "Table"])
        self.combox1.setView(UListV())         # Combo box popup view.
        self.line_ed1 = ULineEd(self.frame2)   # First line edit field.
        self.line_ed1.setPlaceholderText("Full Name...")
        self.line_ed2 = ULineEd(self.frame2)   # Second that for user email.
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
        self.layfr2 = QtWidgets.QGridLayout()  # Layout for second frame.
        self.layfr2.addWidget(self.combox1, 0, 0, 1, 1)
        self.layfr2.addWidget(self.label1, 1, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed1, 2, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed2, 3, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed3, 4, 0, 1, 1)
        self.layfr2.addLayout(self.layfr2_1, 5, 0, 1, 1)
        self.frame2.setLayout(self.layfr2)     # Layout added to frame.
        self.lay1 = QtWidgets.QGridLayout()    # Layout for third widget.
        self.lay1.addWidget(self.frame1, 0, 0, 1, 1)
        self.lay1.addWidget(self.frame2, 0, 1, 1, 1)
        self.twid3.setLayout(self.lay1)        # Set layout to the widget.
        self.mb1.triggered.connect(self.files)
        self.combox1.activated.connect(self.txt_table)
        self.print_device = QtPrintSupport.QPrinter()
        # self.video_camera()                  # Run video camera function.

    def txt_table(self):                       # The function that will
        if self.combox1.currentText() == "Texts":
            self.text_edit.setVisible(True)    # visualize the table and text
            self.table.setVisible(False)       # depends on choice of combo.
        if self.combox1.currentText() == "Table": 
            self.text_edit.setVisible(False)   # When the text activated,
            self.table.setVisible(True)        # elements visible or not.

    def video_camera(self):                    # Function to run videocamera.
        subprocess.Popen(["python", r"u_media.py"])

    def files(self, action):                   # Function open/save files.
        fd = QtWidgets.QFileDialog()           # File dialog instance.
        if action.text() == "Open":            # For opening of the files.
            fdf = fd.getOpenFileNames(self, caption="Open Files",
                                      directory=QtCore.QDir.homePath())
            if len(fdf[0]) > 0:                # Checks if the file dialog
                self.text_edit.clear()         # has a selected files for
                for of in fdf[0]:              # open. Each file of the
                    self.tabwid.setCurrentIndex(2)  # selected will be open. 
                    try:                       # Will try to open file as
                        openf = open(of, 'r')  # simple .txt or .html and, 
                        self.text_edit.append(str(openf.read()))
                        continue               # read content to text field.
                    except Exception:          # If successfull continue.
                        pass                   # If unread or error - pass.
                    try:                       # Try to open file in the 
                        openf = open(of, 'rb') # binary mode .py or other.
                        self.text_edit.append(str(openf.read()))
                    except Exception:          # Content to the field, if 
                        pass                   # error - pass (do nothing).
        if action.text() == "Save":            # For saving of the files.
            fdf = fd.getSaveFileName(self, caption="Save Files",
                                     directory=QtCore.QDir.homePath())
            if fdf[0] != "":                   # Checks if files selected.
                self.tabwid.setCurrentIndex(2) # Open TabWid with Text Field.
                try:                           # Will try to save file as
                    open(fdf[0], 'w').write(self.text_edit.toPlainText())
                    success = True             # .txt file with plain text of
                except Exception:              # text field. And success is 
                    pass                       # True. An error - pass.
                if success != True:            # If file not saved as .txt
                    try:                       # will try to save file in the
                        open(fdf[0], 'wb').write(self.text_edit.toPlainText())
                        success = True         # binary mode, as plain text.
                    except Exception:          # An exception - will pass.
                        pass                   # If success is True will 
                if success == True:            # shown information message.
                    self.info_message(fpath=fdf[0], txt="File saved as",
                                      types="info")
                else:                          # If not True, critical.
                    self.info_message(fpath=fdf[0], txt="File don`t saved",
                                      types="critical")
        if action.text() == "Print":
            print_dialog = QtPrintSupport.QPrintDialog(self.print_device)
            if print_dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.text_edit.print_(print_dialog.printer())
        if action.text() == "Print Preview":   # Print preview dialog.
            print_dialog = QtPrintSupport.QPrintPreviewDialog(self.print_device)
            print_dialog.setWindowTitle("Print Preview")
            print_dialog.setWindowIcon(QtGui.QIcon("Icons/python1.png"))
            print_dialog.paintRequested.connect(self.text_edit.print_)
            print_dialog.exec_()               # Executes dialog window.

    def info_message(self, fpath='', txt='', types="info"):
        message_box = QtWidgets.QMessageBox(self)
        message_box.setStyleSheet("color: #FFFFFF;")
        message_box.setFont(QtGui.QFont("Verdana", 12, 77))
        message_box.setWindowTitle("Save files")
        if types == "info":                    # Function with message box.
            message_box.setIcon(QtWidgets.QMessageBox.Information)
        if types == "critical":                # Critical message box.
            message_box.setIcon(QtWidgets.QMessageBox.Critical) 
        message_box.addButton(QtWidgets.QMessageBox.Ok)
        message_txt = "%s\n%s" %(txt, fpath)   # Adding the button. Text that
        message_box.setText(message_txt)       # will be shown with box.
        message_box.exec_()                    # Shows this message box.


if __name__ == "__main__":                     # If file run, name will main.
    import sys, subprocess                     # Importing stdlib modules.
    from PyQt5 import QtWidgets, QtCore, QtGui
    app = QtWidgets.QApplication(sys.argv)     # Creates application.
    uap = UApp()                               # Main class instance.
    uap.show()                                 # Show the widget when start.
    sys.exit(app.exec_())                      # Executes the application.
