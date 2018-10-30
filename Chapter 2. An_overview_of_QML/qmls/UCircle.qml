import QtQuick 2.7            // For the Rectangle.
import "gradients" as UG      // Import directory with gradients.

Rectangle {                    // Declare Rectangle.
    radius: width * 0.5        // Set radius, rectangle to circle.
    antialiasing: true         // Provide antialiasing.
    layer.enabled: true
    gradient: UG.UGradient1 {} // Imported gradient.
}
