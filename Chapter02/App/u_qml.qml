import QtQuick 2.7                             // QtQuick (MouseArea, other).
import QtQuick.Window 2.2 as UQml              // Our Window as named.
import "qmls" as Uqmls                         // Button, Rectangle, etc.

UQml.Window {                                  // Application Window object.
    visible: true                              // Set visibility property.
    width: 350                                 // Set width.
    height: 590                                // Set height.
    title: qsTr("First Qml")                   // Set title text.
    color: "#000F1F"                           // Set color of the Window.
    Uqmls.URect {                              // Rectangle 1.
        id: rect1                              // Set id attribute.
        signal colored(color uColor)           // Define signal with color
        color: "#000F1F"                       // type. Set hex color.
        width: parent.width                    // Set width of the window.
        property int rzwidth                   // Custom property with width.
        rzwidth: parent.width - (parent.width / 5)
        height: parent.height / 10             // Height of the Rectangle.
        function onUcolor(ucolor) {            // Define method in the QML.
            if (ucolor=="#000F1D") {           // Using if/else construction
                return "#000F1F";              // to realize functionality.
            } else {                           // Function will return white
                return "#000F1D";              // color, if rectangle 1 is
            };                                 // not white, and return
        }                                      // shuttle color if white.
        onColored: rect1.color = onUcolor(rect1.color); 
        MouseArea {                            // Signal handler, color of
            id: marea1                         // the rectangle 1 will be
            anchors.fill: parent               // changed if Area is pressed.
			}                                  // Mouse area, used if
		Connections {                          // clicked. Set id of the
            target: marea1                     // mouse area Position in the
            onClicked: {                       // rectangle. Creates
                rect1.width = rect1.rzwidth;   // connections for the mouse
                rect2.visible = true;          // area. Target MouseArea.
            }                                  // Clicked handler. Clicked
            onPressed: rect1.colored("#000F1F")
        }                                      // signal handler of the Area.
    }                                          // Set color. If area is
    Grid {                                     // clicked, show rectangle 2,
        visible: true                          // and change color of the
        id: grid1                              // rectangle 1. Elements will
        columns: 2                             // be presented with grid
        spacing: 20                            // positioning. Set Id of the 
        padding: 20                            // Grid. Set number of columns 
        width: rect1.width                     // of the grid. Set spacing
        height: parent.height - rect1.height   // between elements of the
        y: rect1.height                        // grid and padding for each
        Uqmls.UCircle {                        // cell of the grid. Width as
            id: circle1                        // Fixed position for the
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width                      // grid. Imported circle 
        }                                      // object as element of the
        Uqmls.URectLG {                        // grid, and set Id. Width as
            id: circle2                        // parent width devided by 2
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width                      // minus right/left spacing
        }                                      // and height as width. Items
        Uqmls.URectRG {                        // used in the grid such as
            id: circle3                        // circles with linear,
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width                      // radial, and conical color
        }                                      // gradients. Unique Id for
        Uqmls.URectCG {                        // item with color gradient.
            id: circle4                        // Width is equal to parent
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width                      // width and spacing
        }                                      // calculation, height to
        Uqmls.URectGlow {                      // parent (Grid) width.
            id: rectg1                         // Imported RectangularGlow
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width                      // object as grid element with
            color: Qt.rgba(0, 0.07, 0.14, 1);  // Id. Width and height
            glowcolor: Qt.rgba(0.007, 1, 1, 1); 
            txglow: Qt.rgba(0.007, 0.7, 0.7, 1);
        }                                      // similar to gradiented
        Uqmls.URectGlow {                      // objects. Rectangle color.
            id: rectg2                         // Glow color. Text glow
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width                      // color, should be some less
            color: Qt.rgba(0, 0.07, 0.14, 1);  // brightnes than glow.  
            glowcolor: Qt.rgba(0.95, 0, 0, 1);
            txglow: Qt.rgba(0.77, 0, 0, 1);    // Used Qt.rgba() to set the
        }                                      // RGBA colors for rectangles,
        Uqmls.URectGlow {                      // glows, and texts that will
            id: rectg3                         // be displayed. The
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width                      // rectangles with glow
            color: Qt.rgba(0, 0.07, 0.14, 1);  // effects are the same
            glowcolor: Qt.rgba(0,0.95,0.37,1);
            txglow: Qt.rgba(0,0.47,0.37,1);    // exclude the colors for
        }                                      // rectangle, glow, and text.
        Uqmls.URectGlow {                      // With last rectangle used
            id: rectg4                         // named colors for glow and
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width                      // text glow. This grid has
            color: Qt.rgba(0, 0.07, 0.14, 1);  // a spacing and padding
            glowcolor: "white";                // properties that describes
            txglow: "grey";                    // the distance between
        }                                      // elements. Two columns
    }                                          // specified for this grid. 
    Uqmls.UItem {                              // Displays the created items
        visible: false                         // in the application window.
        width: rect1.width                     // Set visible to false,
        height: parent.height - rect1.height   // because items will not be
        y: rect1.height                        // visible by default in the
    }                                          // window, can be changed.
    Uqmls.URect {                              // Rectangle 2.
        id: rect2                              // Set id attribute, must be
        visible: false                         // unique. Set visible
        color: "#000F1D"                       // property. Set color
        x: rect1.width                         // property. Position of the
        width: parent.width / 5                // rectangle 2. Set width as
        height: parent.height                  // Window`s width / 5. Set
        Uqmls.UButton {                        // height. Add button object.
            id: ubut1                          // Set id of the button.
            width: rect2.width                 // Set width of the button.
            height: rect2.height / 10          // Set height as parent height
            text: "Hide"                       // devided on 10. Set text
            onClicked: {                       // property. The clicked 
                rect2.visible = false;         // signal handler of the
                rect1.width = UQml.Window.width;
            }                                  // Button. If button is               
        }                                      // clicked, hide rectangle 2
    }                                          // and set width for the 
}                                              // rect 1 to window width.