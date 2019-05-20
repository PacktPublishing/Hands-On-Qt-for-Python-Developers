import QtQuick 2.7                       // Item, Rectangle, Text, MouseArea.
import QtQuick.Layouts 1.3               // Layout importing.
import QtQuick.Controls 1.4              // SplitView importing.

Item {                                   // Item with split view,
    SplitView {                          // the element with possibility to
        anchors.fill: parent; orientation: Qt.Vertical; resizing: true
        Rectangle {                      // choose between text elements and
            id: scr1; color: "#111F1F"   // table representation in the GUI.
            Layout.minimumHeight: parent.height / 2
            Text {                       // The SplitView Type consists the
                id: tx1; anchors.centerIn: parent
                text: "Texts"; color: "grey"
                font: {                  // rectangles as elements of split
                    font.pixelSize=scr1.width / 8;
                    font.letterSpacing=5;
                    font.weight=Font.ExtraBold;
                }                        // with text and mouse area hover
            }                            // and click functionality. The
            MouseArea {                  // onEnterd and onExited handlers
                id: ma1; anchors.fill: parent; hoverEnabled: true
                onEntered: scr1.color = "lightgrey";
                onExited: scr1.color = "#111F1F";
                onClicked: {             // provides the hover effect and
                    txs1.visible = true; grid1.visible = false;
                    main_item = false; tb1.visible = false;
                }                        // onClicked the click event by
            }                            // the element inside split view
        }                                // area. The split element will be
        Rectangle {                      // as part of the right panel with
            id: scr2; color: "#111F1F";  // buttons. Also this element can
            Text {                       // be resized with mouse that    
                id: tx2; anchors.centerIn: parent 
                text: "Table"; color: "grey" 
                font: {                  // demonstrates the functionality of
                    font.pixelSize=scr1.width / 8;
                    font.letterSpacing=5;
                    font.weight=Font.ExtraBold;
                }                        // the split view. The height of the
            }                            // elements is equal to height of
            MouseArea {                  // the parent item divided by two
                id: ma2; anchors.fill: parent; hoverEnabled: true
                onEntered: scr2.color = "lightgrey";
                onExited: scr2.color = "#111F1F";
                onClicked: {             // with relation to the two elements
                    tb1.visible = true; grid1.visible = false;
                    main_item = false; txs1.visible = false;
                }                        // of the split view. In other case
            }                            // the split will visualize just
        }                                // one. The onClicked handlers used
    }                                    // to change the visible properties 
}                                        // of text, table, app, and grid.