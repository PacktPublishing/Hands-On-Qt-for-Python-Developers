import QtQuick 2.7                           // Importing the Rectangle.
import QtGraphicalEffects 1.0                // Importing the RadialGradient.
import "gradients" as UG                     // Directory with gradients.

Rectangle {                                  // Declaration of thr Rectangle.
    antialiasing: true                       // Provides antialiasing.
    radius: width * 0.5                      // Set radius for circle.
    RadialGradient {                         // Radial Gradient declaration.
        anchors.fill: parent                 // Have a full parent size.
        angle: 27                            // Angle rotation around center.
        horizontalRadius: parent.width / 2   // Radius will move to circle 
        verticalRadius: parent.height / 2    // effect. Move to the left 
        horizontalOffset: 3                  // on 3 px. Move to the bottom
        verticalOffset: 3                    // on 3 px. Set source, parent
        source: parent                       // of the radial gradient
        cached: false                        // - rectangle. Gradient can be
        gradient: UG.UGradient1 {}           // defined only with visual type
    }                                        // objects, and blend two or 
}                                            // more colors seamlessly.