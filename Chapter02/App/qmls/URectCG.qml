import QtQuick 2.7                          // Importing the Rectangle.
import QtGraphicalEffects 1.0               // Importing the ConicalGradient.
import "gradients" as UG                    // Directory with gradients.

Rectangle {                                 // Declaration of the Rectangle.
    antialiasing: true                      // Provides antialiasing.
    radius: width * 0.5                     // Set radius for circle.
    ConicalGradient {                       // Conical Gradient declaration.
        anchors.fill: parent                // Have a same size as parent.
        angle: 1                            // Set conical angle.
        horizontalOffset: 7                 // Move to the left on 7 px.
        verticalOffset: 5                   // Move to the bottom on 5 px.
        source: parent                      // Set source, parent of  the
        cached: false                       // conical gradient - rectangle.
        gradient: UG.UGradient1 {}          // Gradient can be defined only
    }                                       // with visual type objects,   
}                                           // blend two or more colors.
