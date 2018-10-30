import QtQuick 2.7            // For the Rectangle.
import QtGraphicalEffects 1.0 // For RadialGradient.
import "gradients" as UG      // Import directory with gradients.

Rectangle {                   // Declare Rectangle.
    antialiasing: true        // Provide antialiasing.
    radius: width * 0.5       // Set radius for circle.
    layer.enabled: true
    RadialGradient {          // Radial Gradient declaration.
        anchors.fill: parent  // Gradient have a full parent size.
        angle: 27             // Set angle rotation around center.
        horizontalRadius: parent.width / 2  // Radius will move 
        verticalRadius: parent.height / 2   // to circle effect.
        horizontalOffset: 3   // Move to the left on 3 px.
        verticalOffset: 3     // Move to the bottom on 3 px.
        source: parent        // Set source, parent of  the
        cached: false         // radial gradient - rectangle.
        gradient: UG.UGradient1 {}  // Imported Gradient.
    } // Gradient can be defined only with visual type objects,   
} // such us Rectangle and blend two or more colors seamlessly.