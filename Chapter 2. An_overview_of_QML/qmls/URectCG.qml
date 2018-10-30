import QtQuick 2.7            // For the Rectangle.
import QtGraphicalEffects 1.0 // For ConicalGradient.
import "gradients" as UG      // Import directory with gradients.

Rectangle {                   // Declare Rectangle.
    antialiasing: true        // Provide antialiasing.
    radius: width * 0.5       // Set radius for circle.
    ConicalGradient {          // Conical Gradient declaration.
        anchors.fill: parent  // Have a same size as parent.
        angle: 1             // Set angle.
        horizontalOffset: 7   // Move to the left on 7 px.
        verticalOffset: 5     // Move to the bottom on 5 px.
        source: parent        // Set source, parent of  the
        cached: false         // conical gradient - rectangle.
        gradient: UG.UGradient1 {}  // Imported Gradient.
    } // Gradient can be defined only with visual type objects,   
} // such us Rectangle and blend two or more colors seamlessly.
