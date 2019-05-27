import QtQuick 2.7                           // QtQuick (MouseArea, other).
import QtQuick.Window 2.2 as UQml            // Our Window as named.
import "qmls" as Uqmls                       // Own created Items.

UQml.Window {                                // Window object, parent of the
    visible: true                            // rectangles. Set visible
    width: 350                               // property Set width, set the
    height: 590                              // height, set title text.
    title: qsTr("First Qml")                 // Adding background color of
    color: "#000F1F"                         // the application window.
    Uqmls.URect {                            // Rectangle 1.
        id: rect1                            // Set id attribute.
        signal colored(color uColor)         // Define signal with color
        color: "#000F1F"                     // type. Set hex color. Set
        width: parent.width                  // width of the window.
        property int rzwidth                 // Custom property with width.
        rzwidth: parent.width - (parent.width / 5)
        height: parent.height / 10           // Set height of the Rectangle.
        onColored: rect1.color = uColor;     // Signal handler, color
                                             // of the rectangle 1 will be
        MouseArea {                          // changed. Mouse area, used if
            id: marea1                       // clicked. Set id of the mouse
            anchors.fill: parent             // area. Position of the area in
        }                                    // this rectangle. Create
        Connections {                        // connections for the mouse
            target: marea1                   // area. Set target as MouseArea.
            onClicked: {                     // Clicked handler. Clicked
                rect1.width = rect1.rzwidth; 
                rect2.visible = true;        // signal handler of the Area.
            }                                // Set new color if clicked.
            onPressed: rect1.colored("#002737") 
        }                                    // If this area is clicked, show
    }                                        // rectangle 2, and change color
    Uqmls.URect {                            // of the rect 1. Rectangle 2.
        id: rect2                            // Set id attribute, must be
        visible: false                       // unique. Set visible property.
        color: "#000F1D"                     // Set color property.
        x: rect1.width                       // Position of the rectangle 2.
        width: parent.width / 5              // Set width as Window width
        height: parent.height                // devided on 5. Set height
        Uqmls.UButton {                      // property. Add button object.
            id: ubut1                        // Set id of the button.
            width: rect2.width               // Set width of the button.
            height: rect2.height / 10        // Set height - height of the
            text: "Hide"                     // rects devided on 10. Set text
            onClicked: {                     // property. Clicked signal
                rect2.visible = false;       // handler of the Button. If
                rect1.width = UQml.Window.width;
            }                                // button is clicked, hide
        }                                    // rectangle 2, and resize
    }                                        // rectangle 1 to the size of
}                                            // application window.