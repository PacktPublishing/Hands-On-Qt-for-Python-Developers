import QtQuick 2.7                               // QtQuick importing.
import QtQuick.Layouts 1.3                       // Layouts importing. 
import "qmls" as Uqmls                           // Import qmls/ directory.

Rectangle {                                      // Rectangle includes the
    visible: true                                // buttons to start apps.
    color: Qt.rgba(0, 0.07, 0.14, 1);            // Contains 4 buttons with
    GridLayout {                                 // glow effects that whose 
        id: grid1; anchors.fill: parent; visible: true
        function wsize() {                       // arranged with grid layout
            if (width < 590) {return 1;} else {return 2;};
        }                                        // and sizes provided in the
        columns: wsize();                        // PyQt/PySide application
        Uqmls.URectGlow {                        // with number of collumns
            id: g5; Layout.fillWidth: true; Layout.fillHeight: true
            Layout.margins: 20                   // dependent on the width of
            color: Qt.rgba(0, 0.07, 0.14, 1);    // window. First rectangle
            glowcolor: Qt.rgba(0.007, 1, 1, 1);  // with glow effects and
            txglow: Qt.rgba(0.007, 0.7, 0.7, 1); // properties for styling
            txtext: "Camera"                     // this rectangle with text.
            txcolor: Qt.rgba(0.2, 0.2, 0.2, 1)   // Signal to app. MouseArea
            signal clicked();                    // will used to change the
            MouseArea {                          // glow color and text glow
                anchors.fill: parent             // when clicked. Rectangle
                onClicked: {                     // clicked() signal. 
                    g5.glowcolor == Qt.rgba(0.007, 1, 1, 1) ?
                    g5.glowcolor = Qt.rgba(0, 0.07, 0.14, 1) :
                    g5.glowcolor = Qt.rgba(0.007, 1, 1, 1);
                    g5.txglow == Qt.rgba(0, 0.07, 0.14, 1) ?
                    g5.txglow = Qt.rgba(0.007, 1, 1, 1) :
                    g5.txglow = Qt.rgba(0, 0.07, 0.14, 1);
                    g5.clicked();                // onClicked handler will
                }                                // change the colors and
            }                                    // send the clicked signal
        }                                        // that will be used in the
        Uqmls.URectGlow {                        // UApp class to start the
            id: g6; Layout.fillWidth: true; Layout.fillHeight: true
            Layout.margins: 20                   // process. Second rectangle
            color: Qt.rgba(0, 0.07, 0.14, 1);    // that will run rotation of
            glowcolor: Qt.rgba(0.95, 0, 0, 1);   // the second circle. Set
            txglow: Qt.rgba(0.77, 0, 0, 1);      // properties as color, glow
            txtext: "QMLS"                       // and text with glow
            txcolor: Qt.rgba(0.2, 0.2, 0.2, 1)   // effects in the red.
            signal clicked();                    // Signal to app. Will
            MouseArea {                          // change the colors when
                anchors.fill: parent             // clicked as values for
                onClicked: {                     // push in and out.
                    g6.glowcolor == Qt.rgba(0.95, 0, 0, 1) ?
                    g6.glowcolor = Qt.rgba(0, 0.07, 0.14, 1) :
                    g6.glowcolor = Qt.rgba(0.95, 0, 0, 1);
                    g6.txglow == Qt.rgba(0, 0.07, 0.14, 1) ?
                    g6.txglow = Qt.rgba(0.77, 0, 0, 1) :
                    g6.txglow = Qt.rgba(0, 0.07, 0.14, 1);
                    g6.clicked();                // Rectangle clicked() 
                }                                // signal. onClicked handler
            }                                    // will change the colors
        }                                        // and send the clicked
        Uqmls.URectGlow {                        // signal that will be used
            id: g7; Layout.fillWidth: true; Layout.fillHeight: true
            Layout.margins: 20                   // in the UApp class to
            color: Qt.rgba(0, 0.07, 0.14, 1);    // start the process. Third
            glowcolor: Qt.rgba(0,0.95,0.37,1);   // glowed rectangle will
            txglow: Qt.rgba(0,0.47,0.37,1);      // start the radial gradient
            txtext: "JUPYTER"                    // circle by clicking of the
            txcolor: Qt.rgba(0.2, 0.2, 0.2, 1)   // mouse area. Colors are
            signal clicked();                    // green and in the rgba.
            MouseArea {                          // Text - grey. Signal to
                anchors.fill: parent             // app. If rectangle is
                onClicked: {                     // pushed colors will change
                    g7.glowcolor == Qt.rgba(0, 0.95, 0.37, 1) ?
                    g7.glowcolor = Qt.rgba(0, 0.07, 0.14, 1) :
                    g7.glowcolor = Qt.rgba(0, 0.95, 0.37, 1);
                    g7.txglow == Qt.rgba(0, 0.07, 0.14, 1) ?
                    g7.txglow = Qt.rgba(0, 0.47, 0.37, 1) :
                    g7.txglow = Qt.rgba(0, 0.07, 0.14, 1);
                    g7.clicked();                // to the grey. Rectangle
                }                                // clicked() signal.
            }                                    // onClicked handler will
        }                                        // change the colors and
        Uqmls.URectGlow {                        // send the clicked signal
            id: g8; Layout.fillWidth: true; Layout.fillHeight: true
            Layout.margins: 20                   // that will be used in the
            color: Qt.rgba(0, 0.07, 0.14, 1);    // UApp class to start the
            glowcolor: Qt.rgba(1, 1, 1, 1);      // process. Fourth rectangle
            txglow: "grey";                      // will viewed. Set layouts
            txtext: "WEB"                        // margins to spacing
            txcolor: Qt.rgba(0.2, 0.2, 0.2, 1)   // between objects and
            signal clicked();                    // borders of the window.
            MouseArea {                          // Some color property is
                anchors.fill: parent             // named, other rgba. Signal
                onClicked: {                     // to app. Will change
                    g8.glowcolor == Qt.rgba(1, 1, 1, 1) ?
                    g8.glowcolor = Qt.rgba(0, 0.07, 0.14, 1) :
                    g8.glowcolor = Qt.rgba(1, 1, 1, 1);
                    g8.txglow == Qt.rgba(0, 0.07, 0.14, 1) ?
                    g8.txglow = "grey" :
                    g8.txglow = Qt.rgba(0, 0.07, 0.14, 1);
                    g8.clicked();                // colors when pushed grey
                }                                // and when push out to the
            }                                    // white. Rectangle
        }                                        // clicked() signal.
    }                                            // onClicked handler will
}                                                // change the colors.
