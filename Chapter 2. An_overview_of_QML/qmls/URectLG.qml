import QtQuick 2.7            // For the Rectangle.
import QtGraphicalEffects 1.0 // For LinearGradient.
import "gradients" as UG      // Import directory with gradients.

Rectangle {                   // Declare Rectangle.
    antialiasing: true        // Provide antialiasing.
    radius: width * 0.5       // Set radius for circle.
    layer.enabled: true
    LinearGradient {          // Linear Gradient declaration.
        anchors.fill: parent  // Gradient have a full parent size.
        start: Qt.point(0, 0) // Start and end points as Qt points.
        end: Qt.point(parent.height, parent.height)
        source: parent        // Set source, parent of  the
        cached: false         // linear gradient is a rectangle.
        gradient: UG.UGradient1 {}  // Imported Gradient.
    } // Gradient can be defined only with visual type objects,   
} // such us Rectangle and blend two or more colors seamlessly.
