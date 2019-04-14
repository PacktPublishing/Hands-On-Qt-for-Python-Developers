# -*- coding: utf-8 -*-         #   PYTHON 3   #
import os                                      # Import for work with paths.
from PySide2 import QtMultimedia, QtMultimediaWidgets
from PySide2 import QtWidgets, QtCore, QtGui   # Importing the main modules,
from u_style import UBut1                      # Multimedia, Button classes.


class UMedia(QtMultimediaWidgets.QCameraViewfinder):
    
    def __init__(self, parent=None):           # Constructor of the class.
        super(UMedia, self).__init__(parent)   # Initialization of the class.
        self.setWindowTitle("U Camera")        # Title of the application.
        win_icon = QtGui.QIcon("Icons/python1.png")
        self.setWindowIcon(win_icon)           # Set icon for this window.
        self.setWindowOpacity(0.95)            # Set widget opacity.
        self.camera = QtMultimedia.QCamera()   # Video Camera device.
        self.camera.setViewfinder(self)        # Set viewfinder for this
        self.camera.start()                    # camera and start.
        self.cambut1 = UBut1(self, pad=10)     # Button for capture image.
        self.cambut1.setText("Capture")        # Text of the button.
        self.cambut1.setVisible(False)         # Set button visible false.
        self.cambut1.clicked.connect(self.img_capture)
        self.vc_grid = QtWidgets.QGridLayout()
        self.vc_grid.addWidget(self.cambut1, 0, 0, 1, 1)
        self.vc_grid.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(self.vc_grid)           # Sets layout to the widget.
    
    def img_capture(self):                     # Function for capture image.
        image_capture = QtMultimedia.QCameraImageCapture(self.camera)
        image_capture.setCaptureDestination(   # Modes and Destination.
                QtMultimedia.QCameraImageCapture.CaptureToFile)
        self.camera.setCaptureMode(QtMultimedia.QCamera.CaptureStillImage)
        filename = os.path.dirname(os.path.abspath(__file__))
        camera_path = os.path.join(filename, "camera/captures/")
        image_capture.capture(os.path.normpath(camera_path))

    def enterEvent(self, event):               # When mouse pointer enter the
        self.cambut1.setVisible(True)          # widget, button is visible.
    
    def leaveEvent(self, event):               # When mouse pointer leave the
        self.cambut1.setVisible(False)         # widget, button is invisible.


if __name__ == "__main__":                     # If file run, name will main.
    import sys                                 # Import sys python`s stdlib.
    app = QtWidgets.QApplication(sys.argv)     # Create application.
    uap_vc = UMedia()                          # Main lass instance.
    uap_vc.show()                              # Show the widget when start.
    sys.exit(app.exec_())                      # Executes the application.