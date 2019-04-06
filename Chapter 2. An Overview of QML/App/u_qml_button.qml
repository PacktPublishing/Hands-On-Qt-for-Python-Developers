import QtQuick 2.7                             // Import for the MouseArea.
import QtQuick.Window 2.2 as UQml              // Import of the Window.
import "qmls" as Uqmls                         // Importing the components.

UQml.Window {                                  // Declaration of the window.
    visible: true                              // Set visible property.
    width: 350                                 // Set width property.
    height: 590                                // Set height property.
    title: qsTr("First Qml")                   // Set title property.
    Uqmls.URect {                              // Child object of the window.
        id: rect1                              // Set id attribute.
        color: "#FFFFFF"                       // Set color property.
        property int rzwidth: parent.width - (parent.width / 5)
                                               // Custom property for rect
        width: parent.width                    // on the initialization.
        height: parent.height                  // Property bindings between
        MouseArea {                            // parent and their child
            anchors.fill: parent               // relationships. Mouse
            onClicked: {                       // area object fill to the
                rect1.width = rect1.rzwidth;   // parent. If area is clicked
                rect2.visible = true;          // rectangle 2 will be shown.
            }                                  // The width of this rectangle 
        }                                      // will be equal to the 
    }                                          // custom property rzwidth.
    Uqmls.URect {                              // Nested object of the
        id: rect2                              // window. Set id attribute,
        visible: false                         // must be unique. Set visible
        color: "#00293b"                       // property. Set color
        x: rect1.width                         // property. Set position
        width: parent.width / 5                // property. Set width binding
        height: parent.height                  // property. Set height
        Uqmls.UButton {                        // binding property. Add
            text: "Hide"                       // button object. Set text
            onClicked: {                       // property. Click the button.
                rect2.visible = false;         // Imperative value 
                rect1.width = UQml.Window.width; 
            }                                  // assignment. If the button
        }                                      // is clicked, this hide
    }                                          // rectangle 2 and set width
}                                              // to the Window width.
