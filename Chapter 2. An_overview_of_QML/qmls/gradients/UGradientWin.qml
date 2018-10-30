import QtQuick 2.7
import QtGraphicalEffects 1.0 // For LinearGradient.

LinearGradient {          // Linear Gradient declaration.
    anchors.fill: parent  // Gradient have a full parent size.
    start: Qt.point(0, 0) // Start and end points as Qt points.
    end: Qt.point(parent.height, parent.height)
    source: parent        // Set source, parent of  the
    cached: false         // linear gradient is a rectangle.
    gradient: Gradient {                // Declare Gradient type.
        GradientStop {        // First GradientStop, position
            position: 0.0;    // of the start of the gradient,
            color: Qt.rgba(0.14, 0.077, 0.14, 1); // and color to this position.
        }                     // GradientStop demonstrates where
        GradientStop {        // stoped the color gradient 
            position: 0.27;   // and started new color gradients. 
            color: Qt.rgba(0.077, 0.077, 0.14, 1); // In the Gradient type available 
        }                     // only vertical gradient, or from 
        GradientStop {        // top to bottom of the object.  
            position: 0.534;  // Position - is a real type number,
            color: Qt.rgba(0.07, 0.077, 0.14, 1); // from 0 to 1 and can be  
        }                     // 0.7 or 0.777, that demonstrate  
        GradientStop {        // the gragient of the colors of 
            position: 0.7147; // this position color and color  
            color: Qt.rgba(0, 0.077, 0.14, 1);  // of the position before. If  
        }                     // available just two GradientStop
        GradientStop {        // positions as 0 and 1, the 
            position: 1.0;    // gradient color will consist
            color: Qt.rgba(0, 0.07, 0.14, 1); // two colors. 
        }
    }
}