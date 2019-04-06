import QtQuick 2.7                           // Importing the Rectangle.
import QtGraphicalEffects 1.0                // Importing the LinearGradient.
import "gradients" as UG                     // Directory with gradients.

Rectangle {                                  // Declaration of the Rectangle.
    antialiasing: true                       // Provides the antialiasing.
    radius: width * 0.5                      // Set radius for circle.
    LinearGradient {                         // Linear Gradient declaration.
        anchors.fill: parent                 // Gradient have a parent size.
        start: Qt.point(0, 0)                // Start and end as Qt points.
        end: Qt.point(parent.height, parent.height)
        source: parent                       // Set source, parent of the
        cached: false                        // linear gradient - rectangle.
        gradient: UG.UGradient1 {}           // Gradient can be defined only
    }                                        // with visual type objects,
}                                            // and blend two or more colors.
