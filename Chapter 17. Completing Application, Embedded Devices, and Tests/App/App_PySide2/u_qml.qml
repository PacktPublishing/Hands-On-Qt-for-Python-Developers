import QtQuick 2.7                              // MouseArea, Item, etc.
import QtQuick.Layouts 1.3                      // Layout importing.
import QtQuick.Window 2.2 as UQml               // Window as named.
import QtQuick.Controls 1.4                     // Menu, MenuItem importing.
import QtQuick.Controls.Styles 1.4              // MenuStyle importing.
import "qmls" as Uqmls                          // Button, Rectangle, etc.

UQml.Window {                                   // Application Window object.
    id: w1; visible: true                       // Add id/visible properties.
    width: UQml.Screen.desktopAvailableWidth    // Screen width.
    height: UQml.Screen.desktopAvailableHeight  // Screen height.
    title: qsTr("First Qml"); color: "#000F1F"  // Title text and 
    Uqmls.UAppwin {id: appwin1; visible: false} // window color
    GridLayout {                                // Declare grid positioning.
        id: main_grid1; columns: 1; rows: 1; anchors.fill: parent
        Uqmls.URect {                           // Rectangle 1 with items.
            Layout.column: 0; Layout.row: 0     // First cell.
            Layout.fillWidth: true; Layout.fillHeight: true
            Layout.minimumHeight: w1.height     // Window height.
            id: rect1                           // Id of the rectangle 1.
            color: "#000F1F"                    // Color of the rectangle.
            MouseArea {                         // Create mouse area for the
                id: marea1; anchors.fill: parent
                onClicked: rect2.visible = true;
            }                                   // rectangle 1. With click of  
            Uqmls.UItem {                       // the right panel will
                id: main_item; visible: false; anchors.fill: parent
            }                                   // arise. Item with elements
            Uqmls.UGrid {                       // that animate rectangles.
                id: grid1; anchors.fill: parent; visible: true
                function wsize() {              // GridLayout with animated
                    if (parent.width > 590) {return 4;} else {return 2;};
                }                               // circles and buttons, and
                columns: wsize();               // JS  function to change the
            }                                   // ammount of columns in the
            Uqmls.UTexts {id: txs1; anchors.fill: parent; visible: false}
            Uqmls.UTable {id: tb1; anchors.fill: parent; visible: false}
        }                                       // window depends from screen
    }                                           // resolution. To display the
    GridLayout {                                // text field and table
        id: main_grid2; columns: 1; rows: 1; anchors.fill: parent
        Uqmls.URect {                           // elements in the window.
            Layout.column: 0; Layout.row: 0     // GridLayout for recatngle2.
            Layout.fillWidth: true; Layout.fillHeight: true
            Layout.alignment: Qt.AlignRight     // Rectangle 2 (rigth side).
            Layout.maximumWidth: w1.width / 5   // First column/row. Align to
            id: rect2; visible: false; color: "#000F1D"
            GridLayout {                        // right side, 5 times less.
                id: but_grid; columns: 1; rows: 4; anchors.fill: parent
                Uqmls.UButton {                 // GridLayout for buttons.
                    id: ubut1; Layout.column: 0; Layout.row: 0
                    Layout.maximumHeight: w1.height / 5
                    Layout.fillWidth: true; Layout.fillHeight: true
                    btext: "HIDE"; tooltip: "Hide the panel with buttons"
                    MouseArea {anchors.fill: parent; hoverEnabled: true
                        onEntered: parent.tcolor = Qt.rgba(1, 0, 0, 1); 
                        onExited: parent.tcolor = Qt.rgba(0.2, 0.2, 0.2, 1);
                        onClicked: rect2.visible = false;}
                }                               // Will hide the right panel.
                Uqmls.UButton {                 // The button in the second
                    id: ubut2; Layout.column: 0; Layout.row: 1
                    Layout.maximumHeight: w1.height / 5
                    Layout.fillWidth: true; Layout.fillHeight: true
                    btext: "APPS"; tooltip: "Run the Application Window"
                    SequentialAnimation {       // row. Animation for the
                        id: sa1; running: false; loops: 1
                        PropertyAnimation {     // button when clicked. 
                            target: ubut2; property: "glrd"; to: 7;
                            duration: 100;      // Second button will blink
                        }                       // with duration as 100
                        PropertyAnimation {     // miliseconds and change the
                            target: ubut2; property: "glrd"; to: 3;
                            duration: 100       // glow radius property of
                        }                       // the UButton at once. Hover
                    }                           // effects, and onClicked
                    MouseArea {anchors.fill: parent; hoverEnabled: true
                        onEntered: parent.tcolor = Qt.rgba(1, 0, 0, 1);
                        onExited: parent.tcolor = Qt.rgba(0.2, 0.2, 0.2, 1);
                        onClicked: {            // handler that starts the
                            sa1.running = true; appwin1.visible = true;
                        }                       // animation and application.   
                    }                           // Third button in the 3 row.
                }                               // If is clicked, will call
                Uqmls.UButton {                 // the button onClicked
                    id: ubut3; Layout.column: 0; Layout.row: 2
                    Layout.fillWidth: true; Layout.fillHeight: true
                    Layout.maximumHeight: w1.height / 5
                    btext: "TOOL"; tooltip: "Show animated rectangles"
                    MouseArea {anchors.fill: parent; hoverEnabled: true
                        onEntered: ubut3.tcolor = Qt.rgba(1, 0, 0, 1);
                        onExited: ubut3.tcolor = Qt.rgba(0.2, 0.2, 0.2, 1);
                        onClicked: ubut3.clicked();
                    }                           // handler. Button onClicked
                    onClicked: {                // handler will display the
                        ubut3.glrd == 3 ? ubut3.glrd = 7 : ubut3.glrd = 3;
                        if (ubut3.glrd==7) {    // layouts with text fields
                            main_item.visible = true; grid1.visible = false;
                            txs1.visible = false; tb1.visible = false;
                        } else {                // and table in the clicking
                            main_item.visible = false; grid1.visible = true;
                            txs1.visible = false; tb1.visible = false;
                        };                      // order sequence. One
                    }                           // visible other invisible.
                }                               // SplitView chooses between
                Uqmls.USplit {                  // the text and table. Is
                    id: spl1; visible: true     // positioned on the 3 row.
                    Layout.column: 0; Layout.row: 3
                    Layout.maximumHeight: w1.height / 5
                    Layout.fillWidth: true; Layout.fillHeight: true
                }                               // Layouts makes interface
            }                                   // resizable and well suited
        }                                       // depends from different
    }                                           // resolutions of the window,
}                                               // item sizes and positions. 