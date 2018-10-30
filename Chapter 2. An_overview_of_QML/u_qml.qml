import QtQuick 2.7                // QtQuick (MouseArea, other).
import QtQuick.Window 2.2 as UQml // Our Window as named.
import "qmls" as Uqmls            // Own created Button, Rectangle, etc.

UQml.Window {                  // Window object.
    visible: true              // Set visibility property.
    width: 350                 // Set width.
    height: 590                // Set height.
    title: qsTr("First Qml")   // Set title text.
    color: "#000F1F"           // Set color of the Window
    Uqmls.URect {              // Rectangle 1.
        id: rect1              // Set id attribute.
        signal colored(color uColor) // Define signal with color type.
        color: "#000F1F"  // Set hex color
        width: parent.width    // Set width of the window.
        property int rzwidth   // Custom property
        rzwidth: parent.width - (parent.width / 5)  // with width.
        height: parent.height / 10  // Set height of the Rectangle.
        function onUcolor(ucolor) {  // Define method in the QML.
            if (ucolor=="#000F1D") { // Using if/else
                return "#000F1F";    // construction to
            } else {                 // realize some
                return "#000F1D";    // functionality.
            }; // Function will return white color, if rectangle 1
        }      // is not white, and return shuttle color if white.
        onColored: rect1.color = onUcolor(rect1.color); // Signal handler, 
        // color of the rectangle 1 will changed if pressed Area.
        MouseArea {            // Mouse area, used if clicked.
            id: marea1     // Set id of the mouse area
            anchors.fill: parent  // Position in the rectangle.
			}
			Connections { // Create connections for the mouse area.
            target: marea1 // Target MouseArea.
            onClicked: {   // clicked handler.
                rect1.width = rect1.rzwidth;
                rect2.visible = true;
            }  // clicked signal handler of the Area.
            onPressed: rect1.colored("#000F1F") // Set color.
        }  // If area is clicked, show rectangle 2,
    }      // and change color of the rectangle 1.
    Grid { // Elements will be presented with grid positioning.
        visible: true
        id: grid1         // Set Id of the Grid.
        columns: 2        // Set number of columns of the grid.
        spacing: 20       // Set spacing between elements of  
        padding: 20       // the grid and padding for each 
        width: rect1.width      // cell of the grid. Width as
        height: parent.height - rect1.height // rectangle 1
        y: rect1.height   // Fixed position for the grid.
        Uqmls.UCircle {   // Imported circle object as element
            id: circle1   // of the grid, and set Id.
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width // Width as parent width devided by 2
        }  // minus right/left spacing and height as width.
        Uqmls.URectLG {
            id: circle2
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width
        }
        Uqmls.URectRG {
            id: circle3
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width
        }
        Uqmls.URectCG {
            id: circle4
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width
        }
        Uqmls.URectGlow { // Imported RectangularGlow object as
            id: rectg1    // grid element with Id. Width and 
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width // height similar to gradient objects.
            color: Qt.rgba(0, 0.07, 0.14, 1); // Rectangle color.
            glowcolor: Qt.rgba(0.007, 1, 1, 1); // Glow color.
            txglow: Qt.rgba(0.007, 0.7, 0.7, 1);// Text glow
        } // color, should be some less brightnes than glow.
        Uqmls.URectGlow {
            id: rectg2
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width
            color: Qt.rgba(0, 0.07, 0.14, 1);
            glowcolor: Qt.rgba(0.95, 0, 0, 1);
            txglow: Qt.rgba(0.77, 0, 0, 1);
        }
        Uqmls.URectGlow {
            id: rectg3
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width
            color: Qt.rgba(0, 0.07, 0.14, 1);
            glowcolor: Qt.rgba(0,0.95,0.37,1);
            txglow: Qt.rgba(0,0.47,0.37,1);
        }
        Uqmls.URectGlow {
            id: rectg4
            width: (parent.width / 2 - (parent.spacing * 2)) + 10
            height: width
            color: Qt.rgba(0, 0.07, 0.14, 1);
            glowcolor: "white";
            txglow: "grey";
        }
    }
    Uqmls.UItem {
        visible: false
        width: rect1.width
        height: parent.height - rect1.height
        y: rect1.height
    }
    Uqmls.URect {               // Rectangle 2.
        id: rect2               // Set id attribute, must be unique.
        visible: false          // Set visibility property.
        color: "#000F1D"        // Set color property.
        x: rect1.width          // Position of the rectangle 2.
        width: parent.width / 5 // Set width as Window width / 5
        height: parent.height   // Set height.
        Uqmls.UButton {         // Add button object.
            id: ubut1           // Set id of the button.
            width: rect2.width  // Set width of the button.
            height: rect2.height / 10  // Set height.
            text: "Hide"         // Set text property.
            onClicked: {
                rect2.visible = false;
                rect1.width = UQml.Window.width;
            } // clicked signal handler of the Button.
        }     // If button is clicked, hide rectangle 2.
    } 
}