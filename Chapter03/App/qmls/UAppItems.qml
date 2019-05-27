import QtQuick 2.7                           // Animations and MouseArea.
import QtQuick.Layouts 1.3                   // Layouts importing. The qmls/
import "." as Qmls                           // directory in the tree.

GridLayout {                                 // Grid Layout construction for
    anchors.centerIn: parent                 // the application, items inside
    columns: 3                               // TabBar that are will be
    Qmls.URectGlow {                         // resized depend on the window
        id: rg1                              // application size. Width and
        Layout.leftMargin: parent.width / 100
        Layout.rightMargin: parent.width / 100
        Layout.topMargin: parent.height / 4
        Layout.bottomMargin: parent.height / 12
        Layout.fillWidth: true               // height are set as fillWidth
        Layout.fillHeight: true              // and fillHeight properties of
        color: Qt.rgba(0, 0.07, 0.14, 1);    // the Layout attached
        glowcolor: Qt.rgba(0.95, 0, 0, 1);   // properties with defining of
        txglow: Qt.rgba(0.77, 0, 0, 1);      // the margins for each side.
        txtext: "PUSH"                       // Items will fill width and
        txcolor: Qt.rgba(0.2, 0.2, 0.2, 1)   // height. Items inside the
        signal acolored(color ucolor)        // application are uses several
        function onAcolor(ucolor) {          // kinds of the animations and
            if (ucolor==Qt.rgba(0.95, 0, 0, 1)) {
                return [Qt.rgba(0.2, 0.2, 0.2, 1), 0.5,
                    Qt.rgba(0, 0.07, 0.14, 1), 0.5,
                    Qt.rgba(0, 0.07, 0.14, 1)];
            } else {                         // functions, where the first
                return [Qt.rgba(0.95, 0, 0, 1), 10,
                    Qt.rgba(0, 0.07, 0.14, 1), 0.1,
                    Qt.rgba(0.77, 0, 0, 1)];
            };                               // kind provides the function
        }                                    // that used to change the color
        onAcolored: {                        // of the glow effect of the
            var acol = onAcolor(rg1.glowcolor) 
            rg1.glowcolor = acol[0];         // rectangle and glow effect 
            rg1.glowr = acol[1];             // of the text inside. Layouts
            rg1.color = acol[2];             // provides the mechanism for
            rg1.spr = acol[3];               // positioning of the items
            rg1.txglow = acol[4];            // without explicit width and
        }                                    // height initialization. As in
        MouseArea {                          // the demonstrations above, the
            anchors.fill: parent             // items with fixed size are not
            onClicked: rg1.acolored(Qt.rgba(0.2, 0.2, 0.2, 1))
        }                                    // have an ability to resizing 
    }                                        // depends from window size.
    Qmls.URectGlow {                         // Some other way to implement
        id: rg2                              // related sizing is usage of
        Layout.leftMargin: parent.width / 100
        Layout.rightMargin: parent.width / 100
        Layout.topMargin: parent.height / 4
        Layout.bottomMargin: parent.height / 12
        Layout.fillWidth: true               // the anchors relation
        Layout.fillHeight: true              // positioning of the items,
        color: Qt.rgba(0, 0.07, 0.14, 1);    // that represent more
        glowcolor: Qt.rgba(0.95, 0, 0, 1);   // convenient way to create a
        txglow: Qt.rgba(0.77, 0, 0, 1);      // flexible construction. The
        txtext: "PUSH"                       // second item provides the 
        txcolor: Qt.rgba(0.2, 0.2, 0.2, 1)   // sequential animation with
        SequentialAnimation {                // effect of the color blinking
            id: sa2; running: false; loops: Animation.Infinite
            PropertyAnimation {              // and changing. In the Property
                target: rg2                  // Animation property with 
                properties: "glowcolor,txglow"
                from: Qt.rgba(0.95, 0, 0, 1);
                to: Qt.rgba(0.007, 1, 1, 1);
                duration: 7000               // string of the properties that
                easing.type: Easing.OutInElastic
            }                                // will be changed when the
            PropertyAnimation {              // MouseArea specified as area
                target: rg2                  // for the rectangle will be
                properties: "glowcolor,txglow"
                from: Qt.rgba(0.007, 1, 1, 1);
                to: Qt.rgba(0.95, 0, 0, 1);  // clicked and blinking will be
                duration: 7000               // started as infinite loop.
                easing.type: Easing.OutInElastic
            }                                // Grid Layout alows to realize  
        }                                    // positioning of the elements
        MouseArea {                          // inside in the grid where each
            anchors.fill: parent; onClicked: sa2.running = true;
        }                                    // item have a cell in the
    }                                        // column and row of the grid
    Qmls.URectGlow {                         // implementation. Also, items
        id: rg3                              // can be arranged with adding
        Layout.leftMargin: parent.width / 100
        Layout.rightMargin: parent.width / 100
        Layout.topMargin: parent.height / 4
        Layout.bottomMargin: parent.height / 12
        Layout.fillWidth: true               // the explicit Layout.row and
        Layout.fillHeight: true              // Layout.column attached
        color: Qt.rgba(0, 0.07, 0.14, 1);    // properties to set the item
        glowcolor: Qt.rgba(0.95, 0, 0, 1);   // position in the row and
        txglow: Qt.rgba(0.77, 0, 0, 1);      // column of the layout.
        txtext: "PUSH"                       // Animations used for the third
        txcolor: Qt.rgba(0.2, 0.2, 0.2, 1)   // rectangle to change them
        ParallelAnimation {                  // properties such as glow
            id: pa3; running: false; loops: Animation.Infinite
            PropertyAnimation {              // color, text glow color, glow
                target: rg3                  // radius and spread of the
                properties: "glowcolor,txglow"
                to: Qt.rgba(0, 0.07, 0.14, 1);
                duration: 7000               // glow of the rectangle at one
                easing.type: Easing.OutInElastic 
            }                                // time and with the duration
            PropertyAnimation {              // in the 7 seconds. Also, can
                target: rg3                  // be implemented a method of 
                properties: "glowr,spr"      // the positioning with Grid,
                to: 1                        // Row, Column Types and using
                duration: 7000               // anchors. The properties of
            }                                // the layout added in the 
        }                                    // items that this grid layout
        MouseArea {                          // will contain. They are
            anchors.fill: parent; onClicked: pa3.running = true
        }                                    // similar and set the margins
    }                                        // for each side betwwen the
}                                            // item and Tab bar window.
