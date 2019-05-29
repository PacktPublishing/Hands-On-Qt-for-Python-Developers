# -*- coding: utf-8 -*-         #   PYTHON 2   #
import u_defaults                              # Setting the default colors,
u_defaults.txt_file(state=False)               # to the application settings.
from u_tools import UTools                     # Importing of the functions.
from u_style import UWid, UFrame, ULabel       # Import the styled widgets.
from u_style import ULineEd, UTextEd           # Import the styled widgets.
from u_style import UComBox, UListV, UTabView  # Import the styled widgets.
from u_style import UBut1                      # Import the styled widgets.
from u_style import UProgress                  # Import the styled widgets.
from u_window import UWindow                   # Importing the Main Window.
from u_table import UTModel                    # Import of the table model.
from PySide2 import QtPrintSupport             # Importing for printing.


class UApp(UWindow, UTools):                   # Create the main class.

    def __init__(self, parent=None):           # Constructor of the class.
        super(UApp, self).__init__(parent)     # Initialization of the class.
        UTools.__init__(self)                  # Initialization of the tools
        # print self.us1                       # class with functions.
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
        self.layfr1.setContentsMargins(0, 0, 0, 0)
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
        self.push_but1 = UBut1(self.frame2)    # Adding the button with text
        self.push_but1.setText("Save")         # For saving operations.
        self.push_but2 = UBut1(self.frame2)    # Adding of the second button.
        self.push_but2.setText("Ok")           # Adding progress bar with
        self.progress1 = UProgress(self.frame2)
        self.progress1.setRange(0, 0)          # range (indeterminate mode).
        self.layfr2_1 = QtWidgets.QGridLayout()
        self.layfr2_1.addWidget(self.push_but1, 0, 0, 1, 1)
        self.layfr2_1.addWidget(self.push_but2, 0, 1, 1, 1)
        self.layfr2_1.addWidget(self.progress1, 1, 0, 1, 2)
        self.layfr2_1.setSpacing(3)            # Spacing for layout - 3 pix.
        self.layfr2 = QtWidgets.QGridLayout()  # Layout for second frame.
        self.layfr2.addWidget(self.combox1, 0, 0, 1, 1)
        self.layfr2.addWidget(self.label1, 1, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed1, 2, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed2, 3, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed3, 4, 0, 1, 1)
        self.layfr2.addLayout(self.layfr2_1, 5, 0, 1, 1)
        self.layfr2.setSpacing(3)              # Sets spacing - 3 pixels.
        self.layfr2.setContentsMargins(3, 3, 3, 3)
        self.frame2.setLayout(self.layfr2)     # Layout added to frame.
        self.lay1 = QtWidgets.QGridLayout()    # Layout for third widget.
        self.lay1.addWidget(self.frame1, 0, 0, 1, 1)
        self.lay1.addWidget(self.frame2, 0, 1, 1, 1)
        self.twid3.setLayout(self.lay1)        # Set layout to the widget.
        self.mb1.triggered.connect(self.files)
        self.mb3.triggered.connect(self.data)  # Connects to the data func.
        self.mb4.triggered.connect(self.options)
        self.combox1.activated.connect(self.txt_table)
        self.push_but1.clicked.connect(self.save_data)
        self.push_but2.clicked.connect(lambda: self.text_edit.setText("HELLO"),
                                       QtCore.Qt.QueuedConnection)
        self.print_device = QtPrintSupport.QPrinter()
        self.actx = ""                         # Empty string for actions.
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

    def options(self, action):                 # Function to run tools by
        if action.text() == "Settings":        # selectection options items.
            from u_settings import USets       # Importing class for color
            self.sets = USets()                # settings, class instance.
            self.sets.show()                   # Shows widget for settings.
            self.sets.bsave.clicked.connect(self.sets_but)
            self.sets.breset.clicked.connect(self.to_default)

    def sets_but(self):                        # Function for "Save" clicks.
        colors = "%s %s %s %s" % (self.sets.bgle1.text(), self.sets.bgle2.text(),
                                  self.sets.colle1.text(), self.sets.colle2.text())
        save_open = open("settings.txt", "w")  # Opens settings.txt file and
        save_open.write(colors)                # writes the colors from line
        save_open.close()                      # edit field, then closes.
        self.new_app()                         # Call the function for new.
    
    def to_default(self):                      # Function to restore the
        u_defaults.txt_file(state=True)        # default colors and calling
        self.new_app()                         # new app in the subprocess.
    
    def new_app(self):                         # Function to re-open new app.
        self.sets.hide()                       # Hides the widget (optional).
        subprocess.Popen(["python", r"u_app.py"])
        sys.exit(0)                            # Run new and exit old app.

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

    def data(self, action):                    # Function for the "Data"
        self.text_edit.clear()                 # panel, if an option will
        self.actx = action.text()              # select, related data will be 
        if self.actx == "Pickle":              # operated with functionality.
            try:                               # Calls the functions that
                txtdata = self.pickle_load(filename=r"data/u_data.py")  
                self.text_edit.append(str(txtdata))
                self.stat_bar.showMessage(self.actx + " opened")
            except Exception as err:           # open/read data from the
                self.stat_bar.showMessage(self.actx + ' ' + str(err))
        if self.actx == "Shelve":              # file/DB and append to
            try:                               # the text edit field.
                db = self.shelve_open(filename="data/u_data")
                self.text_edit.append("%s\n%s\n%s\n%s" % (
                        db.get("User Name"), db.get("User email"),
                        db.get("User password"), db.get("User data")))
                self.stat_bar.showMessage(self.actx + " opened")
            except Exception as err:           # "Pickle" option loads file
                self.stat_bar.showMessage(self.actx + ' ' + str(err))
        if self.actx == "CSV":                 # as text. The "Shelve" loads
            try:                               # data as dictionary values.
                for row in self.csv_read(csvfile="data/tests.csv"):        
                    self.text_edit.append("%s %s %s %s" % (
                            row["User_Name"], row["User_email"],
                            row["User_password"], row["User_data"]))
                self.stat_bar.showMessage(self.actx + " opened")
            except Exception as err:           # "CSV" reads the table
                self.stat_bar.showMessage(self.actx + ' ' + str(err))
        if self.actx == "Pandas":              # with the python standard
            try:                               # library csv module. "Pandas"
                pread = self.pandas_read(filename="data/bigtests.csv",
                                         reader="csv", sep=',')
                def to_field(df, er):          # reads CSV using thread and
                    if er == '':               # nested function, "SQLite"
                        self.text_edit.append("\n" + str(df))
                    else:                      # open and select the values
                        self.stat_bar.showMessage(self.actx + ' ' + er)
                pread.sig1.connect(to_field, QtCore.Qt.QueuedConnection)
                self.stat_bar.showMessage(self.actx + " opened")
            except Exception as err:           # from database. "PostgreSQL"
                self.stat_bar.showMessage(self.actx + ' ' + str(err))
        if self.actx == "SQLite":              # "SQLite" opens and selects
            try:                               # the values from database.
                dbdata = self.sqlite_select()  # "PostgreSQL" opens and
                for dtx in dbdata:             # selects data from database. 
                    self.text_edit.append("%s\n%s\n%s\n%s\n%s" % (
                            dtx[0], dtx[1],dtx[2], dtx[3], dtx[4]))
                self.stat_bar.showMessage(self.actx + " opened")
            except Exception as err:           # "MySQL" opens and selects
                self.stat_bar.showMessage(self.actx + ' ' + str(err))
        if self.actx == "PostgreSQL":          # all values from the MySQL
            try:                               # database, "QtSQL" module of 
                dbdata = self.psql_select()    # the Python binding used
                for dtx in dbdata:             # provides the database 
                    self.text_edit.append("%s\n%s\n%s\n%s\n%s" % (
                            dtx[0], dtx[1], dtx[2], dtx[3], dtx[4]))
                self.stat_bar.showMessage(self.actx + " opened")
            except Exception as err:           # operations of the Qt
                self.stat_bar.showMessage(self.actx + ' ' + str(err))
        if self.actx == "MySQL":               # library, "MongoDB" selects
            try:                               # all values from the NoSQL
                dbdata = self.mysql_select()   # document oriented database 
                for dtx in dbdata:             # MongoDB, and "CouchDB" opens
                    self.text_edit.append("%s\n%s\n%s\n%s\n%s" % (
                            dtx[0], dtx[1], dtx[2], dtx[3], dtx[4]))
                self.stat_bar.showMessage(self.actx + " opened")
            except Exception as err:           # data from the NoSQL CouchDB
                self.stat_bar.showMessage(self.actx + ' ' + str(err))
        if self.actx == "QtSQL":               # database. The text that
            try:                               # retreived from the files and
                dbdata = self.sql_qt_select()  # DB`s appends each value of      
                while dbdata.next():           # the database to the text  
                    self.text_edit.append("%s\n%s\n%s\n%s\n%s" % (    
                            dbdata.value(0), dbdata.value(1), dbdata.value(2),
                            dbdata.value(3), dbdata.value(4)))
                self.stat_bar.showMessage(self.actx + " opened")
            except Exception as err:           # edit field of this app. This
                self.stat_bar.showMessage(self.actx + ' ' + str(err))
        if self.actx == "MongoDB":             # can be changed to the
            try:                               # setText() method that will
                dbdata = self.mongo_select()   # put just last value from the
                for dtx in dbdata:             # query. All tools realized in
                    self.text_edit.append("%s\n%s\n%s\n%s" % (
                            dtx["User Name"], dtx["Email"],
                            dtx["Password"], dtx["Data"]))
                self.stat_bar.showMessage(self.actx + " opened")
            except Exception as err:           # these statements and handle
                self.stat_bar.showMessage(self.actx + ' ' + str(err))
        if self.actx == "CouchDB":             # all Exception errors that
            try:                               # can occur with implementing.
                dbdata = self.couch_select()   # Is recommended to change
                for dtx in dbdata.view("_all_docs", include_docs=True):
                    self.text_edit.append("%s\n%s\n%s\n%s" % (
                            dtx["doc"]["User Name"], dtx["doc"]["User email"],
                            dtx["doc"]["User password"], dtx["doc"]["User Data"]))
                self.stat_bar.showMessage(self.actx + " opened")
            except Exception as err:           # pass to print the errors.
                self.stat_bar.showMessage(self.actx + ' ' + str(err))

    def save_data(self):                       # Function will save the data 
        self.error = ''                        # in relation to used tools.
        uname = self.line_ed1.text()           # User name field value.
        umail = self.line_ed2.text()           # User email field value.
        upass = self.line_ed3.text()           # User password field value.
        udata = self.text_edit.toPlainText()   # Text edit field value.
        if (uname != '') and (umail != '') and (upass != ''):
            if self.actx == "Pickle":          # Pickle option and function.
                self.user_data1(uname, umail, upass, udata)
            elif self.actx == "Shelve":        # Shelve option and function.
                self.user_data2(uname, umail, upass, udata)
            elif self.actx == "CSV":           # CSV option and function.
                self.user_data3(uname, umail, upass, udata)
            elif self.actx == "Pandas":        # Pandas option and function.
                self.user_data4(uname, umail, upass, udata)
            elif self.actx == "SQLite":        # SQLite option and function.
                self.user_data5(uname, umail, upass, udata)
            elif self.actx == "PostgreSQL":    # PostgreSQL option and func.
                self.user_data6(uname, umail, upass, udata)
            elif self.actx == "MySQL":         # MySQL option and function.
                self.user_data7(uname, umail, upass, udata)
            elif self.actx == "QtSQL":         # QtSql option and function.
                self.user_data8(uname, umail, upass, udata)
            elif self.actx == "MongoDB":       # MongoDB option and function.
                self.user_data9(uname, umail, upass, udata)
            elif self.actx == "CouchDB":       # Couch option and function.
                self.user_data10(uname, umail, upass, udata)
            else:                              # By default Pickle function.
                self.user_data1(uname, umail, upass, udata)
            if self.error != '':               # If some errors occur, shows
                self.stat_bar.showMessage(self.actx + ' ' + str(self.error))
            else:                              # error, else shows message.
                self.stat_bar.showMessage(self.actx + " saved")

    def user_data1(self, uname, umail, upass, udata): 
        try:                                   # Function for pickle module.
            dictd = {"User Name": uname, "User email": umail,
                     "User password": upass, "User data": udata}
            self.pickle_dump(obj=dictd, filename=r"data/u_data.py")
        except Exception as err:               # Data as dictionary to file.
            self.error = err                   # If some error - will pass.

    def user_data2(self, uname, umail, upass, udata):
        try:                                   # Function for shelve module.
            db = self.shelve_open(filename="data/u_data")
            db["User Name"] = uname            # Writes user name to DB.
            db["User email"] = umail           # Writes user email to DB.
            db["User password"] = upass        # Writes user password to DB.
            db["User data"] = udata            # Writes user data to DB.
            db.close()                         # Opens database, saves data
        except Exception as err:               # of the text fields to file
            self.error = err                   # and closes database. 

    def user_data3(self, uname, umail, upass, udata):
        fnames = ["User_Name", "User_email", "User_password", "User_data"]
        rdata = [uname, umail, upass, udata[:140]]
        try:                                   # Function to write CSV.
            for row in self.csv_read(csvfile="data/tests.csv"):
                if (row["User_Name"] == rdata[0]) and (
                        row["User_password"] == rdata[2]):
                    rdata = None               # Checks CSV file, if True
        except Exception:                      # data will not be added to
            pass                               # csv file, if erorr - pass. 
        if rdata is not None:                  # If is not None, data will be
            try:                               # added to the CSV file.
                self.csv_write(csvfile="data/tests.csv", fieldnames=fnames,
                               rowdata=rdata, delimiter=' ', lineterminator='\n')
            except Exception as err:           # If some error will occur, 
                self.error = err               # the variable will be error.

    def user_data4(self, uname, umail, upass, udata):  # CSV files with pandas.
        try:                                   # Writing CSV with pandas.
            ucolumns = ["User_Name", "User_email", "User_password", "User_data"]
            self.pandas_write(filename="data/bigtests.csv", writer="csv",
                              columns=ucolumns)
        except Exception as err:               # Put numbers to cells, the
            self.error = err                   # number of rows is 999.

    def user_data5(self, uname, umail, upass, udata):
        try:                                   # SQLite database function.
            self.sqlite_insert(username=uname, email=umail,
                               passw=upass, data=udata)
        except Exception as err:               # Inserts values of the text
            self.error = err                   # edit field to the SQLite DB.

    def user_data6(self, uname, umail, upass, udata):
        try:                                   # PostgreSQL DB function.
            self.psql_insert(username=uname, email=umail,
                             passw=upass, data=udata)
        except Exception as err:               # Inserts values of the text
            self.error = err                   # edit field to PostgreSQL.

    def user_data7(self, uname, umail, upass, udata):
        try:                                   # MySQL database function.
            self.mysql_insert(username=uname, email=umail,
                              passw=upass, data=udata)
        except Exception as err:               # Inserts values of the text
            self.error = err                   # edit field to the MySQL DB.

    def user_data8(self, uname, umail, upass, udata):
        try:                                   # Using QtSql module function.
            self.sql_qt_insert(username=uname, email=umail,
                               passw=upass, data=udata)
        except Exception as err:               # Inserts values of the text
            self.error = err                   # edit field to the SQLite DB.

    def user_data9(self, uname, umail, upass, udata): 
        try:                                   # NoSQL MongoDB function.
            self.mongo_insert(username=uname, email=umail,
                              passw=upass, data=udata)
        except Exception as err:               # Inserts values of the text
            self.error = err                   # edit field to the Mongo DB.

    def user_data10(self, uname, umail, upass, udata):
        try:                                   # To document of the CouchDB.
            self.couch_insert(username=uname, email=umail,
                              passw=upass, data=udata)
        except Exception as err:               # Inserts values of the text
            self.error = err                   # edit field to the Couch DB.


if __name__ == "__main__":                     # If file run, name will main.
    import sys, subprocess                     # Importing stdlib modules.
    from PySide2 import QtWidgets, QtCore, QtGui
    app = QtWidgets.QApplication(sys.argv)     # Creates application.
    uap = UApp()                               # Main class instance.
    uap.show()                                 # Show the widget when start.
    sys.exit(app.exec_())                      # Executes the application.
