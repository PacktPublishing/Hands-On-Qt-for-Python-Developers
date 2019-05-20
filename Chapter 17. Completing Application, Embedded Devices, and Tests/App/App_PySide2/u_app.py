# -*- coding: utf-8 -*-         #   PYTHON 2   #
import time                                    # Working with time/date.
import u_defaults                              # Setting values, colors,
u_defaults.txt_file(state=False)               # to the application settings.
from u_tools import UTools                     # Importing UTools class.
from u_style import UFrame, ULabel             # Importing styled widgets.
from u_style import ULineEd, UTextEd           # Importing styled widgets.
from u_style import UComBox, UListV, UTabView  # Importing styled widgets.
from u_style import UBut1                      # Importing styled widgets.
from u_style import UProgress                  # Importing styled widgets.
from u_style import UGraphView                 # Importing styled widgets.
from u_window import UWindow                   # Importing the Main Window.
from u_widget import UWidget                   # Importing the Widget.
from u_table import UTModel                    # Import of the table model.
from PySide2 import QtPrintSupport             # Importing Printer support.
from PySide2 import QtQuickWidgets             # Importing for using QML. 
from u_gitems import GRectItem


class UApp(UWindow, UTools):                   # The main class of the GUI.

    def __init__(self, parent=None):           # Constructor of the class.
        super(UApp, self).__init__(parent)     # Initialization of the class.
        UTools.__init__(self)                  # Initialization of the tools
        print self.us1                         # class with functions.
        self.apps = QtQuickWidgets.QQuickWidget(self.twid1)
        self.apps.setSource(QtCore.QUrl("apps.qml"))
        self.properties = self.apps.rootObject()
        self.gscene = QtWidgets.QGraphicsScene()
        self.gview = UGraphView(self.twid2)    # Adding of the graphics view
        self.painter = QtGui.QPainter()        # to the tab widget, adding
        self.gvlay = QtWidgets.QGridLayout()   # scene and painter that can
        self.gvlay.addWidget(self.gview, 0, 0, 1, 1)
        self.gvlay.setContentsMargins(0, 0, 0, 0)  
        self.twid2.setLayout(self.gvlay)       # used, arrange with grid.
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
        self.frame1.setLayout(self.layfr1)     # Layout for this field.
        self.frame2 = UFrame(self.twid3)       # Second Frame with parent.
        self.frame2.setLineWidth(3)            # Sets line width of the frame
        self.frame2.setFrameStyle(0)           # and 0 - style No frame.
        self.frame2.setMaximumWidth(int(self.width()/3))
        self.label1 = ULabel(self.frame2)      # Label for the second frame. 
        self.label1.setText("User Information")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.combox1 = UComBox(self.frame2)    # Add the combobox with items.
        self.combox1.addItems(["Texts", "Table"])
        self.combox1.setView(UListV())         # Combo popup list view.
        self.line_ed1 = ULineEd(self.frame2)   # Line edit with placeholder.
        self.line_ed1.setPlaceholderText("Full Name...")
        self.line_ed2 = ULineEd(self.frame2)   # Second will for user email.
        self.line_ed2.setPlaceholderText("Email...")
        self.line_ed3 = ULineEd(self.frame2)   # Third field for password,
        self.line_ed3.setPlaceholderText("Password...")  
        self.line_ed3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.push_but1 = UBut1(self.frame2)    # Adding button with text
        self.push_but1.setText("Save")         # for saving operations.
        self.push_but2 = UBut1(self.frame2)    # Adding button with text
        self.push_but2.setText("Ok")           # for other operations.
        self.progress1 = UProgress(self.frame2)
        self.progress1.setRange(0, 0)          # Progress bar with range.
        self.layfr2_1 = QtWidgets.QGridLayout()
        self.layfr2_1.addWidget(self.push_but1, 0, 0, 1, 1)
        self.layfr2_1.addWidget(self.push_but2, 0, 1, 1, 1)
        self.layfr2_1.addWidget(self.progress1, 1, 0, 1, 2)
        self.layfr2_1.setSpacing(3)            # Widgets spacing for layout.
        self.layfr2 = QtWidgets.QGridLayout()  # Second frame`s layout.
        self.layfr2.addWidget(self.combox1, 0, 0, 1, 1)
        self.layfr2.addWidget(self.label1, 1, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed1, 2, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed2, 3, 0, 1, 1)
        self.layfr2.addWidget(self.line_ed3, 4, 0, 1, 1)
        self.layfr2.addLayout(self.layfr2_1, 5, 0, 1, 1)
        self.layfr2.setSpacing(3)              # Spacing between widgets.
        self.layfr2.setContentsMargins(3, 3, 3, 3)
        self.frame2.setLayout(self.layfr2)     # Set layout to second frame.
        self.lay1 = QtWidgets.QGridLayout()    # Layout for the third tabwid.
        self.lay1.addWidget(self.frame1, 0, 0, 1, 1)
        self.lay1.addWidget(self.frame2, 0, 1, 1, 1)
        self.twid3.setLayout(self.lay1)        # Adding fdf.values[0]rames to tab widget.
        self.mb1.triggered.connect(self.files)
        self.mb2.triggered.connect(self.edit)  # Calling files, edit, data,
        self.mb2_1.triggered.connect(self.edit_align)
        self.mb3.triggered.connect(self.data)  # optins, and help function.
        self.mb4.triggered.connect(self.options)
        self.mb5.triggered.connect(self.on_help)
        self.qmlbut1 = self.properties.childItems()[0].childItems()[0]
        self.qmlbut1.clicked.connect(self.video_camera)
        self.qmlbut2 = self.properties.childItems()[0].childItems()[1]
        self.qmlbut2.clicked.connect(self.qml_apps)
        self.qmlbut3 = self.properties.childItems()[0].childItems()[2]
        self.qmlbut3.clicked.connect(self.jupyter)
        self.qmlbut4 = self.properties.childItems()[0].childItems()[3]
        self.qmlbut4.clicked.connect(self.web_browse)
        self.combox1.activated.connect(self.txt_table)
        self.push_but1.clicked.connect(self.save_data)
        self.push_but2.clicked.connect(self.vis)
        self.print_device = QtPrintSupport.QPrinter()
        self.actx = ""                         # Empty string for actions.
        self.qapp1 = 0                         # Value for the qml button 1.
        self.qapp2 = 0                         # Value for the qml button 2.
        self.qapp3 = 0                         # Value for the qml button 3.
        self.qapp4 = 0                         # Value for the qml button 4.

    def long_loop(self):                       # Function for starting the
        while True:                            # while instruction.
            QtWidgets.qApp.processEvents(QtCore.QEventLoop.AllEvents)
            print("HELLO")                     # Will print string.

    def vis(self):                             # Set the 2d tab widget as
        self.tabwid.setCurrentIndex(1)         # current, set device window
        desktop = QtWidgets.QApplication.desktop()
        self.setGeometry(desktop.availableGeometry())
        self.visualize()                       # size, and call the function.

    def visualize(self):                       # Function visualizes data.
        self.gscene.clear()                    # Clear current graphics scene
        self.gview.resetCachedContent()        # with reset cache content.
        self.gview.setScene(self.gscene)       # Sets scene to the view with
        self.gview.setSceneRect(self.gscene.sceneRect())
        self.pen = QtGui.QPen()                # scene rectangle. Creates pen
        self.scw = float(self.tabwid.currentWidget().width() - 30)
        self.sch = float(self.tabwid.currentWidget().height() - 30)
        try:                                   # that used to draw lines.
            dline = self.draws(w=self.scw, h=self.sch)
            def to_line(xy, er):               # Will be called when thread
                if er == '':                   # will emit signal with data.
                    color = QtGui.QColor("#00D9FF")
                    cmyk = color.toCmyk()      # Changing of the color used
                    c = cmyk.cyanF()           # with pen. The particles of
                    m = cmyk.magentaF() * float(1/xy[1])
                    y = cmyk.yellowF() * float(1/xy[1])
                    k = cmyk.blackF() * float(1/xy[1])
                    a = cmyk.alphaF()          # CMYK, alpha-transparency.
                    color.setCmykF(c, m, y, k, a)
                    self.pen.setColor(color)   # Set new color to pen and
                    self.gscene.addLine(QtCore.QLineF(xy[1], self.sch,
                                                      xy[1], xy[0]), self.pen)
                else:
                    self.stat_bar.showMessage(self.actx + ' ' + er)
            dline.sig1.connect(to_line, QtCore.Qt.QueuedConnection)
        except Exception as err:               # draw line with new position.
            self.stat_bar.showMessage(self.actx + ' ' + str(err))

    def resizeEvent(self, event):              # Resize event handler.
        self.properties.setWidth(float(self.tabwid.currentWidget().width()))
        self.properties.setHeight(float(self.tabwid.currentWidget().height()))

    def video_camera(self):                    # Function, run video camera.
        self.qapp1 += 1                        # Will add to this variable 1
        if self.qapp1 == 1:                    # when button will be clicked.
            # subprocess.Popen(["python", r"u_media.py"])
            self.approc1 = QtCore.QProcess()   # Run procces with QProcces
            self.approc1.start("python", ["u_media.py"])   # 
        if self.qapp1 == 2:                    # startung file with Python.
            self.approc1.kill()                # If the button clicked at
            self.qapp1 = 0                     # second, kills process. 

    def qml_apps(self):                        # Function to sart QML apps.
        self.qapp2 += 1                        # Runs the file with starting
        if self.qapp2 == 1:                    # instructions for QML`s.
            # subprocess.Popen(["python", r"u_qml.py"])
            self.approc2 = QtCore.QProcess()   # The QProcess uses the start
            self.approc2.start("python", ["u_qml.py"])
        if self.qapp2 == 2:                    # function with command to run
            self.approc2.kill()                # with Python and file name in
            self.qapp2 = 0                     # the working directory.

    def jupyter(self):                         # Function to sart Jupyter.
        self.qapp3 += 1                        # Runs the jupyter available
        if self.qapp3 == 1:                    # in the Anaconda toolset.
            # subprocess.Popen(["jupyter", ["notebook", "--browser=firefox"])
            self.approc3 = QtCore.QProcess()   # The QProcess uses the start
            self.approc3.start("jupyter", ["notebook", "--browser=firefox"])
        if self.qapp3 == 2:                    # command to run jupyter
            self.approc3.kill()                # notebook with specified
            self.qapp3 = 0                     # browser that can be changed.

    def web_browse(self):                      # Function to sart webbrowser.
        self.qapp4 += 1                        # Runs the default web browser
        if self.qapp4 == 1:                    # available in the system.
            # subprocess.Popen("python", ["-m", "webbrowser", "-n",
            #                            "https://www.python.org"])
            self.approc4 = QtCore.QProcess()   # The QProcess uses the start
            self.approc4.start("python", ["-m", "webbrowser", "-n",
                                          "https://www.python.org"])
        if self.qapp4 == 2:                    # command to open the URL of
            self.approc4.kill()                # the page that is specified
            self.qapp4 = 0                     # in the default browser.

    def txt_table(self):                       # The function that will
        if self.combox1.currentText() == "Texts":
            self.text_edit.setVisible(True)    # visualize the table and text
            self.table.setVisible(False)       # depends on choice of combo.
        if self.combox1.currentText() == "Table": 
            self.text_edit.setVisible(False)   # When the text activated,
            self.table.setVisible(True)        # elements visible or not.

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

    def edit(self, action):                    # Function for editing of the
        if action.text() == "Undo":            # text edit field content.
            self.text_edit.undo()              # Undoes, Redoes, Cut, Copy,
        if action.text() == "Redo":            # Paste simple operations.
            self.text_edit.redo()              # Selected text will be copied
        if action.text() == "Cut":             # to, or pasted from the
            self.text_edit.cut()               # buffer if available, the
        if action.text() == "Copy":            # action indicates which
            self.text_edit.copy()              # option is selected. The
        if action.text() == "Paste":           # "Text Color" and "Text Font"
            self.text_edit.paste()             # will operate with changing
        if action.text() == "Text Color":      # of the current Font and 
            self.fd = QtWidgets.QColorDialog() # Color of the selected text.
            if self.fd.exec_() == QtWidgets.QDialog.Accepted:
                fc = self.fd.selectedColor()   # First dialog inherits the
                self.text_edit.setTextColor(fc)
        if action.text() == "Text Font":       # Main Window and have a 
            self.fd = QtWidgets.QFontDialog()  # similar style. Second Font
            if self.fd.exec_() == QtWidgets.QDialog.Accepted:
                ft = self.fd.selectedFont()    # dialog have not a parent
                self.text_edit.setFont(ft)     # and have default style.

    def edit_align(self, action):              # Function for submenu option
        if action.text() == "center":          # text edit field alignment.
            self.text_edit.setAlignment(QtCore.Qt.AlignCenter)
        if action.text() == "left":            # Will align the text by
            self.text_edit.setAlignment(QtCore.Qt.AlignLeft)
        if action.text() == "right":           # center, to left, to right,
            self.text_edit.setAlignment(QtCore.Qt.AlignRight)
        if action.text() == "justify":         # or justified of the field.
            self.text_edit.setAlignment(QtCore.Qt.AlignJustify)

    def options(self, action):                 # Function to run tools by
        if action.text() == "Settings":        # selectection options items.
            from u_settings import USets       # Importing class for color
            self.sets = USets()                # settings, class instance.
            self.sets.show()                   # Widget for color settings.
            self.sets.bsave.clicked.connect(self.sets_but)
            self.sets.breset.clicked.connect(self.to_default)
        if action.text() == "Run":             # Option will run execution
            action.setEnabled(False)           # of the script from text 
            datas = self.text_edit.toPlainText()
            try:                               # edit filed and will append
                self.text_edit.append("\n\n\n\n\nRESULT -----------> %s\n" %
                                      time.strftime("%Y.%m.%d %H:%M:%S"))
                runs = self.run_code(datas=datas)
                def to_field(sto, ste, er):    # the result to text filed.
                    if er == '':               # For running the code used
                        self.text_edit.append(str(sto) + "\n" + str(ste))
                    else:                      # thread and class that moved
                        self.stat_bar.showMessage(er)
                runs[1].sig1.connect(to_field, QtCore.Qt.QueuedConnection)
                runs[0].quit()                 # to this thread. Called
                def on_stop():                 # function returns the tuple
                    action.setEnabled(True)    # with thread and class. Sends
                runs[0].finished.connect(on_stop)
            except Exception as err:           # finished signal from thread.
                self.stat_bar.showMessage(str(err))
        if action.text() == "Configuration":   # Option for check current
            def get_info():                    # working environment. Checks
                if self.uwid1.infocomb.currentIndex() == 0:
                    try:                       # Anaconda available packages
                        condinf = subprocess.Popen(["conda", "list"],
                                                   stdout=subprocess.PIPE)
                        conp = condinf.communicate()
                        self.uwid1.infotxt.setText(conp[0].decode("utf-8"))
                    except Exception as err:
                        self.uwid1.infotxt.setText(str(err))
                if self.uwid1.infocomb.currentIndex() == 1:
                    try:                       # and Python packages that
                        condinf = subprocess.Popen(["pip", "list"],
                                                   stdout=subprocess.PIPE)
                        conp = condinf.communicate()
                        self.uwid1.infotxt.setText(
                                """Platform: %s\nPython %s version
                                \nPython path list: %s\n\nRecursion limit: %s
                                \nFilesystem encoding: %s\nDefault encoding: %s
                                \nAvailable installed packages: \n\n%s""" %
                                (sys.platform, sys.version, sys.path,
                                 sys.getrecursionlimit(),
                                 sys.getfilesystemencoding(),
                                 sys.getdefaultencoding(), conp[0].decode("utf-8")))
                    except Exception as err:   # installed with pip. Option
                        self.uwid1.infotxt.setText(str(err))
            self.uwid1 = UWidget()             # for "pip" use various tools
            self.uwid1.setWindowTitle("Configuration")
            self.uwid1.infocomb.addItems(["conda", "pip"])
            self.uwid1.infotxt.setReadOnly(True)
            self.uwid1.infotxt.setVisible(True)
            self.uwid1.show()                  # of the sys module for info.
            self.uwid1.infocomb.activated.connect(get_info)

    def on_help(self, action):                 # Function realizes the help
        if action.text() == "Online Help":     # option of the top panel.
            self.uwid2 = UWidget()             # Using widget for visualize
            self.uwid2.setWindowTitle("Online Help")
            self.uwid2.infocomb.setVisible(False)
            self.uwid2.infotxt.setReadOnly(True)
            self.uwid2.infotxt.setVisible(False)
            self.uwid2.wview.setVisible(True)  # online documentation and
            html = open("help.html", "r").read()
            self.uwid2.wview.setHtml(html)     # help from remote resources,
            self.uwid2.show()                  # "Online Help" sets existed
        if action.text() == "Documentation":   # .html file with script. 
            def get_docs():                    # "Documentation" option load
                if self.uwid3.infocomb.currentIndex() == 0:
                    try:                       # URLs to the Web Engine View
                        self.uwid3.wview.load( # and visualize documentation
                                QtCore.QUrl("https://docs.python.org/3/"))
                    except Exception as err:   # from the sources specified.
                        self.stat_bar.showMessage(str(err))
                if self.uwid3.infocomb.currentIndex() == 1:
                    try:                       # The base widget is used to 
                        self.uwid3.wview.load( # arrange web view and combo
                                QtCore.QUrl("https://www.riverbankcomputing.com/static/Docs/PyQt5/"))
                    except Exception as err:   # in the separate window.
                        self.stat_bar.showMessage(str(err))
                if self.uwid3.infocomb.currentIndex() == 2:
                    try:                       # The nested functions checks
                        self.uwid3.wview.load( # which option of the combobox
                                QtCore.QUrl("https://doc.qt.io/qtforpython/index.html"))
                    except Exception as err:   # is selected and load URL.
                        self.stat_bar.showMessage(str(err))
            self.uwid3 = UWidget()             # Combobox use activated()
            self.uwid3.setWindowTitle("Documentation")
            self.uwid3.infocomb.addItems(["Python", "PyQt5", "PySide2"])
            self.uwid3.infotxt.setReadOnly(True)
            self.uwid3.infotxt.setVisible(False)
            self.uwid3.wview.setVisible(True)  # signal to connect the nested
            self.uwid3.show()                  # function. Sets Visibility.
            self.uwid3.infocomb.activated.connect(get_docs)

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
        sys.exit(0)                            # Run new application window.

    def info_message(self, fpath='', txt='', types="info"):
        message_box = QtWidgets.QMessageBox(self)
        message_box.setStyleSheet("color: #FFFFFF;")
        message_box.setFont(QtGui.QFont("Verdana", 12, 77))
        message_box.setWindowTitle("Save files")
        if types == "info":                    # Function for message boxes
            message_box.setIcon(QtWidgets.QMessageBox.Information)
        if types == "critical":                # Icons for this message box.
            message_box.setIcon(QtWidgets.QMessageBox.Critical) 
        message_box.addButton(QtWidgets.QMessageBox.Ok)
        message_txt = "%s\n%s" %(txt, fpath)   # Text that will be used with
        message_box.setText(message_txt)       # this boxes and buttons.
        message_box.exec_()                    # executes and show the box.

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
        if self.actx == "MongoDB":             # receives the data to the
            try:                               # text edit field, can be
                mongo_data = self.mongo_select()
                def to_field(dbdata, er):      # changed to the setText()
                    if er == '':               # method that will put just
                        for dtx in dbdata:     # last value from the query.
                            self.text_edit.append("%s\n%s\n%s\n%s" % (
                                    dtx["User Name"], dtx["Email"],
                                    dtx["Password"], dtx["Data"]))
                    else:                      # All tools realized in
                        self.stat_bar.showMessage(self.actx + ' ' + er)
                mongo_data.sig1.connect(to_field, QtCore.Qt.QueuedConnection)
                self.stat_bar.showMessage(self.actx + " opened")
            except Exception as err:           # statement and handle all
                self.stat_bar.showMessage(self.actx + ' ' + str(err))
        if self.actx == "CouchDB":             # Exception errors. The errors
            try:                               # represented in the status
                couch_data = self.couch_select()
                def to_field(dbdata, er):      # bar and can contain the 
                    if er == '':               # standard errors or related
                        for dtx in dbdata.view("_all_docs", include_docs=True):
                            self.text_edit.append("%s\n%s\n%s\n%s" % (
                                    dtx["doc"]["User Name"],
                                    dtx["doc"]["User email"],
                                    dtx["doc"]["User password"],
                                    dtx["doc"]["User Data"]))
                    else:                      # errors to the used packages
                        self.stat_bar.showMessage(self.actx + ' ' + er)
                couch_data.sig1.connect(to_field, QtCore.Qt.QueuedConnection)
                self.stat_bar.showMessage(self.actx + " opened")
            except Exception as err:           # in the application.
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
