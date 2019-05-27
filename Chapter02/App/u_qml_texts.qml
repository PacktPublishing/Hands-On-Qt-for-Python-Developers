import QtQuick 2.7                                 // Import for MouseAre.
import QtQuick.Window 2.2 as UQml                  // Import for Window.
import "qmls" as Uqmls                             // Imorting Items.

UQml.Window {                                      // Window declaration.
    visible: true                                  // Window wil be visible. 
    width: 350                                     // Width in the pixels.
    height: 590                                    // Height in the pixels.
    title: qsTr("First Qml")                       // Title of the window.
    Uqmls.URect {                                  // First rectangle.
        id: rect1                                  // Id attribute.
        color: "#000000"                           // Color of the rectangle.
        width: parent.width - (parent.width / 5)   // Width as window width
        height: parent.height                      // minus window width
        Uqmls.UText {                              // devided on 5. Height
            id: utext1                             // as window height. The
            x: 20                                  // first text item.
            y: 50                                  // With absolute x-axis
            font.family: "Open"                    // and y-axis position.
            font.pixelSize: 37                     // X-axis is a position
            width: rect1.width - (20 * 2)          // from top-left corner of
            text: "text 1"                         // the widow to right.
        }                                          // Y-axis position from
        Uqmls.UText {                              // top-left corner to
            id: utext2                             // bootom. Second text. 
            x: 20                                  // Id must be unique.
            y: utext1.height + (50 * 2)            // Position. Font family
            font.family: "Verdana"                 // of the text, size of
            font.pixelSize: 27                     // text in pixels, Width
            width: rect1.width - (20 * 2)          // of the text that is
        }                                          // equal to the parrent
        Uqmls.UText {                              // rectangle width minus
            id: utext3                             // number that equal to
            x: 20                                  // to position of the text
            y: (utext1.height + utext2.height) + (50 * 3)
            font.family: "Open Sans"               // on the rectangle by the 
            font.pointSize: 14                     // x-axis that have been
            width: rect1.width - (20 * 2)          // multiplied on the two,
        }                                          // for the best view.
        MouseArea {                                // Mouse area of this
            anchors.fill: parent                   // rectangle. Size of the
            onClicked: rect1.color = "#222222";    // MouseArea is equal to
        }                                          // rectangle. When will
    }                                              // click - change color.
    Uqmls.URect {                                  // Second rectangle.
        id: rect2                                  // Id attribute.
        color: "#00293b"                           // Color of the rectangle.
        x: rect1.width                             // Position by the x-axis.
        width: parent.width / 5                    // Width as window devided 
        height: parent.height                      // on 5, and window`s
        MouseArea {                                // height. Rectangle area,
            anchors.fill: parent                   // size is equal to this 
            onClicked: {                           // rectangle, when clicked
                rect2.color = "#340147";           // change rectangle color
                utext2.text = "text 2";            // to the specified, set
                utext3.text = "text 3";            // text to the first text 
            }                                      // object and second. For
        }                                          // these operations are
    }                                              // used identifiers for
}                                                  // each represented item.
