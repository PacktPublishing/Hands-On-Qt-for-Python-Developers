# -*- coding: utf-8 -*-         #   PYTHON 2   #
from PySide2 import QtWidgets, QtCore, QtGui   # Import the PySide2 modules.

setfile = open("settings.txt", "r")            # Colors for widgets in file.
colread = setfile.read().split(" ")            # Read, split by space string
if len(colread) == 4:                          # to list with 4 items.
    color = colread                            # If the file will be changed
else:                                          # unexpectedly and lenght of
    color = ["", "", "", ""]                   # color list not equal to 4,
setfile.close()                                # will be with empty strings.


class UFonts(object):                          # Will change the fonts.
    
    def __init__(self, parent=None, ls=2.0, ws=2.0, family="Verdana",
                 size=12, weight=34):          # Parameters of the fonts.
        self.font1 = QtGui.QFont()             # Sets fonts to widgets.
        self.font1.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, ls)
        self.font1.setWordSpacing(ws)          # Set spacing between letters
        self.font1.setFamily(family)           # and words, sets font family,
        self.font1.setPixelSize(size)          # sets font size in the pixels
        self.font1.setWeight(weight)           # and font weight of the text.


class UWin(QtWidgets.QMainWindow):             # Class for Main Window.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UWin, self).__init__(parent)     # initialization.
        self.setWindowTitle("U App")           # Title of the application
        win_icon = QtGui.QIcon("Icons/python1.png")
        self.setWindowIcon(win_icon)           # Sets icon.
        self.setWindowOpacity(1)               # Sets widget opacity.
        self.setAnimated(True)                 # Set property  enabled.
        self.setAcceptDrops(True)              # Accept drop event.
        self.setMouseTracking(True)            # Mouse tracking enabled.
        self.setUpdatesEnabled(True)           # Updates enabled.
        self.setAutoFillBackground(True)       # Auto fill of the background.
        self.setStyleSheet("background-color: %s;" % (color[0],))


class UMBar(QtWidgets.QMenuBar):               # Class for Menu Bar.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UMBar, self).__init__(parent)    # initialization.
        self.setStyleSheet("background-color: %s;" % (color[2],))


class UMenu(QtWidgets.QMenu):                  # Class for Menu.

    def __init__(self, parent=None):           # Constructor of the class and
        super(UMenu, self).__init__(parent)    # initialization.
        self.setStyleSheet("background-color: %s;" % (color[2],))


class UTWid(QtWidgets.QTabWidget):             # Class for Tab Widget.

    def __init__(self, parent=None, twbdr=3, twbdw=0.5, twbbg=color[1],
                 tbpad=7, tbsize=140, tbbg=color[0], tbc=color[2],
                 tbcs=color[3]):               # Constructor with parameters.
        super(UTWid, self).__init__(parent)    # initialization of ab widget.
        font = UFonts()                        # Fonts with default params.
        self.setFont(font.font1)               # Sets font to the tab widget.
        self.twbdr = twbdr                     # Parameters of the __init__
        self.twbdw = twbdw                     # function of the class,
        self.twbbg = twbbg                     # that will be used in the
        self.tbsize = tbsize                   # functions of this class to
        self.tbpad = tbpad                     # styling. Parameters of the 
        self.tbbg = tbbg                       # borders size, background
        self.tbc = tbc                         # colors, text colors, size of
        self.tbcs = tbcs                       # the tabs in the tab bar. Set
        self.setStyleSheet(                    # parameters with StyleSheet. 
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
        super(USBar, self).__init__(parent)    # initialization.
        self.setStyleSheet("background-color: %s;" % (color[2],))


class UWid(QtWidgets.QWidget):                 # Class for Widget.

    def __init__(self, parent=None, bg=color[1], bgh=color[3], minw=0, minh=0,
                 maxw=None, maxh=None, fixw=None, fixh=None, mrg=0, pad=0,
                 bds="solid", bdr=3, bdw=0, bdc=color[3]):
        super(UWid, self).__init__(parent)     # initialization of the widget.
        self.setWindowTitle("U App")           # Title of the application
        win_icon = QtGui.QIcon("Icons/python1.png")  # QIcon path
        self.setWindowIcon(win_icon)           # Set icon.
        self.setWindowOpacity(0.95)            # Set widget opacity.
        self.setAcceptDrops(True)              # Accept drop event.
        self.setMouseTracking(True)            # Mouse tracking enabled.
        self.setUpdatesEnabled(True)           # Updates enabled.
        self.setAutoFillBackground(True)       # Auto fill for background.
        self.setMinimumWidth(minw)             # Minimum width of the widget.
        self.setMinimumHeight(minh)            # Minimum height of widget.
        if maxw is not None:                   # By default, max width None.
            self.setMaximumWidth(maxw)         # Maximum width of the widget.
        if maxh is not None:                   # By default, max height None.
            self.setMaximumHeight(maxh)        # Maximum height of widget.
        if fixw is not None:                   # If the fixed width parameter
            self.setFixedWidth(fixw)           # not None, sets fixed width.
        if fixh is not None:                   # If fixed height parameter
            self.setFixedHeight(fixh)          # not None, sets fixed height.
        self.bg, self.bgh, self.mrg, self.pad = bg, bgh, mrg, pad
        self.bds, self.bdr, self.bdw, self.bdc = bds, bdr, bdw, bdc
        self.setStyleSheet(self.wid_style(self.mrg, self.pad, self.bg, self.bds,
                                          self.bdr, self.bdw, self.bgh))

    def wid_style(self, mrg=None, pad=None, bg=None, bds=None, bdr=None,
                  bdw=None, bdc=None):         # Function for styling.
        style = """margin: %spx; padding: %spx; background-color: %s;
                border-style: %s; border-radius: %spx; border-width: %spx;
                border-color: %s;""" % (mrg, pad, bg, bds, bdr, bdw, bdc)
        return style                           # Returns style for using.

    def enterEvent(self, event):               # Mouse enters this widget.
        self.setStyleSheet(self.wid_style(self.mrg, self.pad, self.bgh, self.bds,
                                          self.bdr, self.bdw, self.bdc))

    def leaveEvent(self, event):               # Mouse leaves the widget.
        self.setStyleSheet(self.wid_style(self.mrg, self.pad, self.bg, self.bds,
                                          self.bdr, self.bdw, self.bdc))


class UFrame(QtWidgets.QFrame):                # Class for Frame.

    def __init__(self, parent=None, sbh=7, sbv=7, sbc=color[1]):
        super(UFrame, self).__init__(parent)   # Initialization of the frame.
        self.sbh = sbh                         # Set style for the scroll,
        self.sbv = sbv                         # background color of the 
        self.sbc = sbc                         # scroll, width, height.
        self.setStyleSheet(                    # Styling of this Frame.
                    """QFrame {background-color: %s;}
                       QScrollBar:horizontal {width: %spx; height: %spx;
                                        background-color: %s;}
                       QScrollBar:vertical {width: %spx; height: %spx;
                                        background-color: %s;}"""
                              % (color[2], self.sbh, self.sbh, self.sbc,
                                 self.sbv, self.sbv, self.sbc))


class ULabel(QtWidgets.QLabel):                # Class for Label.

    def __init__(self, parent=None):           # Constructor of the class and
        super(ULabel, self).__init__(parent)   # initialization of the label.
        font = UFonts(ls=3.0, size=14, weight=59)
        self.setFont(font.font1)               # Sets font with params.
        self.setStyleSheet(                    # Styling of the Label,
                """background-color: %s; color: %s;""" 
                % (color[0], color[3]))        # background and text colors.


class ULineEd(QtWidgets.QLineEdit):            # Class for Line Edit field.

    def __init__(self, parent=None, tmrgl=10, tmrgt=10, tmrgr=10, tmrgb=10,
                 drg=True, bdr=5, bdw=1, bdc=color[3]):
        super(ULineEd, self).__init__(parent)  # initialization of the field.
        self.setClearButtonEnabled(True)       # Button to clear input.
        self.setDragEnabled(drg)               # Set drag enabled and text 
        self.setTextMargins(tmrgl, tmrgt, tmrgr, tmrgb)  # margins to each
        self.bdr = bdr                         # side from params of the 
        self.bdw = bdw                         # __init__, such as border
        self.bdc = bdc                         # radius, width and color.
        font = UFonts(size=14, weight=59)      # The class for font changes.
        self.setFont(font.font1)               # Sets font with params.
        self.setStyleSheet(                    # Styling of the Line Edit,
                """background-color: %s; color: %s; border-radius: %spx;
                border-width: %spx; border-color: %s;""" 
                % (color[0], color[3], self.bdr, self.bdw, self.bdc))


class UTextEd(QtWidgets.QTextEdit):            # Class for Text Edit field.

    def __init__(self, parent=None, bgcolor=color[0], sbh=7, sbv=7,
                 sbc=color[1], tepad=7, tebgcolor=color[1], tetxc=color[3],
                 lh=14, bdr=5, bdw=1, bdc=color[3]):
        super(UTextEd, self).__init__(parent)  # initialization of the field.
        self.setAcceptRichText(True)           # Rich text will accepted.
        self.setUndoRedoEnabled(True)          # undoes and redoes enabled.
        self.bgcolor = bgcolor                 # Properties from __init__
        self.sbh = sbh                         # function to set style for:
        self.sbv = sbv                         # background color of the 
        self.sbc = sbc                         # widget, width, height and
        self.tepad = tepad                     # background color for scroll
        self.tebgcolor = tebgcolor             # bars of the text field, 
        self.tetxc = tetxc                     # padding for text field from 
        self.lh = lh                           # text field frame to texts,
        self.bdr = bdr                         # text color, background color
        self.bdw = bdw                         # of the field, line height of
        self.bdc = bdc                         # the text and field borders.
        font = UFonts(size=14, weight=59)      # The class for font changes.
        self.setFont(font.font1)               # Sets font with parameters.
        self.setStyleSheet(                    # Styling of the Text Edit.
                """QWidget {background-color: %s;}
                   QScrollBar:horizontal {width: %spx; height: %spx;
                                          background-color: %s;}
                   QScrollBar:vertical {width: %spx; height: %spx;
                                        background-color: %s;}
                   QTextEdit {padding: %spx; background-color: %s;
                              color: %s; line-height: %spx;
                              border-style: solid; border-radius: %spx;
                              border-width: %spx; border-color: %s;}"""
                              % (self.bgcolor, self.sbh, self.sbv, self.sbc,
                                 self.sbh, self.sbv, self.sbc, self.tepad,
                                 self.tebgcolor, self.tetxc, self.lh,
                                 self.bdr, self.bdw, self.bdc))


class UComBox(QtWidgets.QComboBox):            # Class for Combo Box field.

    def __init__(self, parent=None, icon=None, pad=10, bdr=5, bdw=1, bdc=color[3]):
        super(UComBox, self).__init__(parent)  # initialization of the field.
        self.icon = icon
        self.pad = pad                         # Parameters for this combobox
        self.bdr = bdr                         # that can be changed with
        self.bdw = bdw                         # new values of the padding
        self.bdc = bdc                         # and border properties.
        font = UFonts(size=14, weight=59)
        self.setFont(font.font1)               # Sets font with params.
        self.setStyleSheet("""QComboBox {padding: %spx; background-color: %s;
                                         color: %s; border-style: solid;
                                         border-radius: %spx; border-width: %spx;
                                         border-color: %s;}
                              QComboBox:drop-down:down-arrow {
                                      image: url(%s); width: 14px; height: 14px;}
                              QComboBox:drop-down:button {margin: %spx;
                                                          background-color: %s;
                                                          border-style: solid;
                                                          border-radius: %spx;
                                                          border-width: %spx;
                                                          border-color: %s;}
                              """ 
                              % (self.pad, color[0], color[3], self.bdr,
                                 self.bdw, self.bdc, self.icon, self.pad,
                                 color[0], self.bdr, self.bdw, self.bdc))



class UListV(QtWidgets.QListView):             # Class for List View.

    def __init__(self, parent=None, mg=5, pad=10, bdr=5, bdw=1, bdc=color[3]):
        super(UListV, self).__init__(parent)   # List view initialization.
        self.setWordWrap(True)                 # Sets word wrap by words.
        self.mg = mg                           # Parameters for this list
        self.pad = pad                         # view with margin, padding,
        self.bdr = bdr                         # border radius, border
        self.bdw = bdw                         # width and border color,
        self.bdc = bdc                         # can be change with using.
        font = UFonts(size=14, weight=59)      # Using fonts for list view
        self.setFont(font.font1)                     # popup display, size, weight.
        self.setStyleSheet("""margin: %spx; padding: %spx; background-color: %s;
                           color: %s; border-style: solid; border-radius: %spx;
                           border-width: %spx; border-color: %s;"""
                           % (self.mg, self.pad, color[0], color[3], self.bdr,
                              self.bdw, self.bdc))


class UTabView(QtWidgets.QTableView):          # Class for Table View.

    def __init__(self, parent=None, tvpad=7, tvbgcolor=color[1],
                 tvtxc=color[3], bdr=5, bdw=1, bdc=color[3]):
        super(UTabView, self).__init__(parent) # Table view initialization.
        self.tvpad = tvpad                     # Properties from __init__,
        self.tvbgcolor = tvbgcolor             # such as background color, 
        self.tvtxc = tvtxc                     # padding, grid line color
        self.bdr = bdr                         # text color, border color,
        self.bdw = bdw                         # border width and border
        self.bdc = bdc                         # radius for table view.
        font = UFonts(size=14, weight=59)      # Font size and weight.
        self.setFont(font.font1)               # Sets font with parameters.
        self.setStyleSheet(                    # Styling of the Table View.
                """QTableView {padding: %spx; background-color: %s;
                              color: %s; border-style: solid;
                              border-radius: %spx; border-width: %spx;
                              border-color: %s; gridline-color: %s;}"""
                              % (self.tvpad, self.tvbgcolor, self.tvtxc,
                                 self.bdr, self.bdw, self.bdc, color[3]))


class UBut1(QtWidgets.QPushButton):            # Class for Push Buttons.

    def __init__(self, parent=None, bg="rgba(9,219,190,140)",
                 bgh="rgba(9,219,190,255)", txc="rgba(1,255,255,190)",
                 txch="rgba(1,255,255,255)", minw=0, minh=0, maxw=None, maxh=None,
                 fixw=None, fixh=None, mrg=0, pad=7, bds="solid", bdr=3,
                 bdw=0, bdc=color[3], checks=False):
        super(UBut1, self).__init__(parent)    # Button initialization.
        self.setFlat(True)                     # Set button without borders.
        self.setMouseTracking(True)            # Mouse tracking available.
        self.setMinimumWidth(minw)             # Minimum width of the button.
        self.setMinimumHeight(minh)            # Minimum height of button.
        if maxw is not None:                   # By default, maxwidth None.
            self.setMaximumWidth(maxw)         # Maximum width of the button.
        if maxh is not None:                   # By default, maxheight None.
            self.setMaximumHeight(maxh)        # Maximum height of button.
        if fixw is not None:                   # If the fixed width parameter
            self.setFixedWidth(fixw)           # is not None, fixed width.
        if fixh is not None:                   # If fixed height parameter
            self.setFixedHeight(fixh)          # is not None, fixed height.
        self.checks = checks                   # If parameter is True, sets
        self.setCheckable(self.checks)         # this button as checkable.
        self.bg, self.bgh, self.txc, self.txch = bg, bgh, txc, txch      
        self.mrg, self.pad = mrg, pad          # Parameters to style sheet.
        self.bds, self.bdr, self.bdw, self.bdc = bds, bdr, bdw, bdc
        self.setStyleSheet(self.but_style(self.mrg, self.pad, self.bg, self.txc,
                                          self.bds, self.bdr, self.bdw, self.bgh))

    def but_style(self, mrg=None, pad=None, bg=None, txc=None, bds=None,
                  bdr=None, bdw=None, bdc=None):
        style = """margin: %spx; padding: %spx; background-color: %s;
        color: %s; border-style: %s; border-radius: %spx; border-width: %spx;
        border-color: %s;""" % (mrg, pad, bg, txc, bds, bdr, bdw, bdc)
        return style                           # Returns style that be used.

    def resizeEvent(self, event):              # Function will used with
        self.fonts = UFonts(size=int((self.width() + self.height())/self.pad),
                            weight=100)        # resizing of the button,
        self.setFont(self.fonts.font1)         # changes the fonts.

    def enterEvent(self, event):               # Mouse enters to this button.
        self.setStyleSheet(self.but_style(self.mrg, self.pad, self.bgh, self.txch,
                                          self.bds, self.bdr, self.bdw, self.bdc))

    def leaveEvent(self, event):               # Mouse leaves the button.
        self.setStyleSheet(self.but_style(self.mrg, self.pad, self.bg, self.txc,
                                          self.bds, self.bdr, self.bdw, self.bgh))


class UProgress(QtWidgets.QProgressBar):       # Class for Progress Bar.

    def __init__(self, parent=None, bg="rgba(0,190,255,140)",
                 txc="rgba(1,255,255,190)", minw=0, minh=0, maxw=None,
                 maxh=None, fixw=None, fixh=None, mrg=0, pad=7,
                 bds="solid", bdr=3, bdw=0, bdc=color[3]):
        super(UProgress, self).__init__(parent)
        self.setMinimumWidth(minw)             # Minimum width of the bar.
        self.setMinimumHeight(minh)            # Minimum height of the bar.
        if maxw is not None:                   # By default, max width None.
            self.setMaximumWidth(maxw)         # Maximum width of the bar.
        if maxh is not None:                   # By default, max height None.
            self.setMaximumHeight(maxh)        # Maximum height of the bar.
        if fixw is not None:                   # If the fixed width parameter
            self.setFixedWidth(fixw)           # is not None, fixed width.
        if fixh is not None:                   # If fixed height parameter
            self.setFixedHeight(fixh)          # is not None, fixed height.
        self.bg, self.txc, self.mrg, self.pad = bg, txc, mrg, pad     
        self.bds, self.bdr, self.bdw, self.bdc = bds, bdr, bdw, bdc
        self.setStyleSheet(self.pgrs_style(self.mrg, self.pad, self.bg, self.txc,
                                          self.bds, self.bdr, self.bdw, color[2]))
        
    def pgrs_style(self, mrg=None, pad=None, bg=None, txc=None, bds=None,
                   bdr=None, bdw=None, bdc=None):
        style = """QProgressBar {margin: %spx; padding: %spx; border-style: %s;
                    border-radius: %spx; border-width: %spx; border-color: %s;}
                   QProgressBar::chunk {background-color: %s; color: %s;}
                """ % (mrg, pad, bds, bdr, bdw, bdc, bg, txc)
        return style                           # Returns new style for bar.


class UGraphView(QtWidgets.QGraphicsView):     # Class for Graphics View.

    def __init__(self, parent=None, bg=color[1], bgh=color[3], minw=0, minh=0,
                 maxw=None, maxh=None, fixw=None, fixh=None, mrg=0, pad=0,
                 bds="solid", bdr=3, bdw=0, bdc=color[3]):
        super(UGraphView, self).__init__(parent)
        self.setAcceptDrops(True)              # Accept drop event.
        self.setMouseTracking(True)            # Mouse tracking enabled.
        self.setUpdatesEnabled(True)           # Updates enabled.
        self.setAutoFillBackground(True)       # Auto fill background enabled.
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setMinimumWidth(minw)             # Minimum width of the view.
        self.setMinimumHeight(minh)            # Minimum height of the view.
        if maxw is not None:                   # By default, max width None.
            self.setMaximumWidth(maxw)         # Maximum width of the view.
        if maxh is not None:                   # By default, max height None.
            self.setMaximumHeight(maxh)        # Maximum height of the view.
        if fixw is not None:                   # If the fixed width parameter
            self.setFixedWidth(fixw)           # not None, sets fixed width.
        if fixh is not None:                   # If fixed height parameter
            self.setFixedHeight(fixh)          # not None, sets fixed height.
        self.bg, self.bgh, self.mrg, self.pad = bg, bgh, mrg, pad
        self.bds, self.bdr, self.bdw, self.bdc = bds, bdr, bdw, bdc
        self.setStyleSheet(self.gview_style(self.mrg, self.pad, self.bg, self.bds,
                                          self.bdr, self.bdw, self.bgh))

    def gview_style(self, mrg=None, pad=None, bg=None, bds=None, bdr=None,
                    bdw=None, bdc=None):       # Function for styling view.
        style = """margin: %spx; padding: %spx; background-color: %s;
        border-style: %s; border-radius: %spx; border-width: %spx;
        border-color: %s;""" % (mrg, pad, bg, bds, bdr, bdw, bdc)
        return style
