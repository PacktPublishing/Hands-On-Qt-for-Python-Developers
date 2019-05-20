import QtQuick 2.7                       // Importing Gradient, GradientStop.
import QtGraphicalEffects 1.0            // Importing the LinearGradient.

LinearGradient {                         // Linear Gradient declaration.
    anchors.fill: parent                 // Gradient have a full parent size.
    start: Qt.point(0, 0)                // Start and end points as Qt points.
    end: Qt.point(parent.height, parent.height)
    source: parent                       // Set source, parent of the
    cached: false                        // linear gradient is a rectangle.
    gradient: Gradient {                 // Declare Gradient type.
        GradientStop {                   // First GradientStop, position
            position: 0.0;               // of the start of the gradient.
            color: Qt.rgba(0.14, 0.077, 0.14, 1);
        }                                // GradientStop demonstrates where
        GradientStop {                   // stoped the color gradient 
            position: 0.27;              // and started new color gradients. 
            color: Qt.rgba(0.077, 0.077, 0.14, 1);
        }                                // available only vertical gradient,
        GradientStop {                   // or from top to bottom.  
            position: 0.534;             // Position - is a real type number,
            color: Qt.rgba(0.07, 0.077, 0.14, 1); 
        }                                // from 0.0 to 1.0 and can be 0.7 
        GradientStop {                   // or 0.777, that demonstrate the 
            position: 0.7147;            // gragient of the colors of this
            color: Qt.rgba(0, 0.077, 0.14, 1);
        }                                // position color and color of the
        GradientStop {                   // position before. If available
            position: 1.0;               // just two GradientStop positions
            color: Qt.rgba(0, 0.07, 0.14, 1);
        }                                // as 0 and 1, the  gradient color
    }                                    // will consist two colors. This
}                                        // gradient used in the app window.