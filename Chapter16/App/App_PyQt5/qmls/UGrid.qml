import QtQuick 2.7                             // QtQuick Grid importing.
import QtQuick.Layouts 1.3                     // Layouts importing. 
import "." as Uqmls                            // Gradiented, glowed objects. 

GridLayout {                                   // New grid layout instead the
    Uqmls.UCircle {id: g1;Layout.margins: 20   // simple grid. Set the items
    Layout.fillWidth: true;Layout.fillHeight: true}
    Uqmls.URectLG {id: g2;Layout.margins: 20   // to the layout with sizes
    Layout.fillWidth: true;Layout.fillHeight: true}
    Uqmls.URectRG {id: g3;Layout.margins: 20   // that as grid layout parent
    Layout.fillWidth: true;Layout.fillHeight: true}
    Uqmls.URectCG {id: g4;Layout.margins: 20   // size. Sets first rectangle
    Layout.fillWidth: true;Layout.fillHeight: true}
    Uqmls.URectGlow {                          // with the glow effects and
        id: g5; Layout.fillWidth: true; Layout.fillHeight: true
        Layout.margins: 20                     // properties for styling this
        color: Qt.rgba(0, 0.07, 0.14, 1);      // rectangle with text. The
        glowcolor: Qt.rgba(0.007, 1, 1, 1);    // MouseArea will be used to 
        txglow: Qt.rgba(0.007, 0.7, 0.7, 1);   // change the glow color and
        txtext: "PUSH"                         // text glow if is clicked.
        txcolor: Qt.rgba(0.2, 0.2, 0.2, 1)     // The onClicked handler will 
        MouseArea {                            // change the colors and run
            anchors.fill: parent               // this animations when
            onClicked: {                       // clicked. Animator for
                g5.glowcolor == Qt.rgba(0.007, 1, 1, 1) ?
                g5.glowcolor = Qt.rgba(0, 0.07, 0.14, 1) :
                g5.glowcolor = Qt.rgba(0.007, 1, 1, 1);
                g5.txglow == Qt.rgba(0, 0.07, 0.14, 1) ?
                g5.txglow = Qt.rgba(0.007, 1, 1, 1) :
                g5.txglow = Qt.rgba(0, 0.07, 0.14, 1);
                g5a.running == true ?          // rotation the item. Will
                g5a.running = false : g5a.running = true;
            }                                  // rotate clockwise the item 
        }                                      // with id g1 to 360 degrees,
        RotationAnimator {                     // duration is 1 second. Than 
            id: g5a; running: false; loops: Animation.Infinite
            target: g1                         // less duration then rotation
            to: 360                            // will be more fast. This
            duration: 1000                     // animation will be infinite.
            easing.type: Easing.Linear         // Second rectangle that will  
        }                                      // run rotation of the second
    }                                          // circle. Set properties as
    Uqmls.URectGlow {                          // color, glow and text with
        id: g6; Layout.fillWidth: true; Layout.fillHeight: true
        Layout.margins: 20                     // glow effects in the red.
        color: Qt.rgba(0, 0.07, 0.14, 1);      // That will change the colors
        glowcolor: Qt.rgba(0.95, 0, 0, 1);     // if the area will be clicked
        txglow: Qt.rgba(0.77, 0, 0, 1);        // with new values for push in
        txtext: "PUSH"                         // and out this rectangle.
        txcolor: Qt.rgba(0.2, 0.2, 0.2, 1)     // Will run the rotation when
        MouseArea {                            // push in and stop when out. 
            anchors.fill: parent               // MouseArea`s onClicked
            onClicked: {                       // signal handler changes the
                g6.glowcolor == Qt.rgba(0.95, 0, 0, 1) ?
                g6.glowcolor = Qt.rgba(0, 0.07, 0.14, 1) :
                g6.glowcolor = Qt.rgba(0.95, 0, 0, 1);
                g6.txglow == Qt.rgba(0, 0.07, 0.14, 1) ?
                g6.txglow = Qt.rgba(0.77, 0, 0, 1) :
                g6.txglow = Qt.rgba(0, 0.07, 0.14, 1);
                g6a.running == true ?          // colors of glow and text
                g6a.running = false : g6a.running = true;
            }                                  // glow dependent on the  
        }                                      // click state, push in/out.
        RotationAnimator {                     // Animator for rotation.
            id: g6a; running: false; loops: Animation.Infinite
            target: g2                         // Circle 2 will be rotated
            to: 360                            // by 360 degrees, faster than
            duration: 300                      // first by signed duration
            easing.type: Easing.InQuad         // that less than in the first
        }                                      // type with accelerating
    }                                          // from the zero velocity.
    Uqmls.URectGlow {                          // Third glowed rectangle will 
        id: g7; Layout.fillWidth: true; Layout.fillHeight: true
        Layout.margins: 20                     // start the radial gradient
        color: Qt.rgba(0, 0.07, 0.14, 1);      // circle by clicking of the
        glowcolor: Qt.rgba(0,0.95,0.37,1);     // mouse area. The colors are
        txglow: Qt.rgba(0,0.47,0.37,1);        // green and in the rgba.
        txtext: "PUSH"                         // Text - grey. If this
        txcolor: Qt.rgba(0.2, 0.2, 0.2, 1)     // rectangle is pushed in, the
        MouseArea {                            // colors will change to the
            anchors.fill: parent               // grey. The margins arround
            onClicked: {                       // item in the layout will be  
                g7.glowcolor == Qt.rgba(0, 0.95, 0.37, 1) ?
                g7.glowcolor = Qt.rgba(0, 0.07, 0.14, 1) :
                g7.glowcolor = Qt.rgba(0, 0.95, 0.37, 1);
                g7.txglow == Qt.rgba(0, 0.07, 0.14, 1) ?
                g7.txglow = Qt.rgba(0, 0.47, 0.37, 1) :
                g7.txglow = Qt.rgba(0, 0.07, 0.14, 1);
                g7a.running == true ?          // equal to 20 pixels.
                g7a.running = false : g7a.running = true;grid1 
            }                                  // Starting the third circle
        }                                      // with radial gradient to
        RotationAnimator {                     // rotate. Set to the animator
            id: g7a; running: false; loops: Animation.Infinite
            target: g3                         // the id, run to false, will
            to: 360                            // running with push in the 
            duration: 200                      // area and with duration
            easing.type: Easing.InCubic        // to 0.2 seconds that will
        }                                      // provide fast rotation
    }                                          // around self axis with cubic
    Uqmls.URectGlow {                          // easing type. The fourth
        id: g8; Layout.fillWidth: true; Layout.fillHeight: true
        Layout.margins: 20                     // rectangle will be viewed.
        color: Qt.rgba(0, 0.07, 0.14, 1);      // Set layouts margins to
        glowcolor: Qt.rgba(1, 1, 1, 1);        // spacing between objects and
        txglow: "grey";                        // borders of the window. Some
        txtext: "PUSH"                         // color properties are named,
        txcolor: Qt.rgba(0.2, 0.2, 0.2, 1)     // other rgba. Will change the
        MouseArea {                            // colors, if pushed - to the
            anchors.fill: parent               // grey and if pushed out - to
            onClicked: {                       // the white color. Will start
                g8.glowcolor == Qt.rgba(1, 1, 1, 1) ?
                g8.glowcolor = Qt.rgba(0, 0.07, 0.14, 1) :
                g8.glowcolor = Qt.rgba(1, 1, 1, 1);
                g8.txglow == Qt.rgba(0, 0.07, 0.14, 1) ?
                g8.txglow = "grey" :           // the rotation of the fourth
                g8.txglow = Qt.rgba(0, 0.07, 0.14, 1);
                g8a.running == true ?          // circle with conical color
                g8a.running = false : g8a.running = true;
            }                                  // gradient that will colorize 
        }                                      // clockwize. This example
        RotationAnimator {                     // demonstrates the advantages
            id: g8a; running: false; loops: Animation.Infinite
            target: g4                         // of the layout items
            to: 360                            // positioning constructions
            duration: 100                      // as the most convenient way
            easing.type: Easing.InQuart        // to set items and make them 
        }                                      // resizable dependent from
    }                                          // the window or parent width
}                                              // and height relations.
