import QtQuick 2.7                       // Importing the Rectangle QML type.
import QtGraphicalEffects 1.0            // Importing the RectangularGlow.

Rectangle {                              // Box for the glowing rectangle.
    property color glowcolor             // Custom property, glow color.
    property color txglow                // Custom property, text glow color.
    RectangularGlow {                    // RectangularGlow, must to be 
        id: rglow                        // placed before the rectangle which  
        anchors.fill: rectglow           // will be glow to get the effect.
        glowRadius: 10                   // Radius of the glow around.
        spread: 0.1                      // Spread of the glow, decreasing
        color: glowcolor                 // to more distortion of the color.
        cornerRadius: rectglow.radius + glowRadius
    }                                    // Corner radius of the glow.
    Rectangle {                          // Center rectangle, have a glow
        id: rectglow                     // effect with color similar to the 
        color: parent.color              // parent rectangle color.
        anchors.centerIn: parent         // Set to the center in the 
        width: parent.width / 1.5        // parent with width and 
        height: parent.height / 1.5      // height of parent / 1.5.
        radius: 14                       // Radius of the rectangle corners.
        Text {                           // Text into rectangle will glow
            id: txt1                     // as rectangle but with Glow Type.
            anchors.centerIn: parent     // Set text to the center of the
            text: "PUSH"                 // parent rectangle. Font family,
            font.family: "Helvetica"     // pixel size of the font depends
            font.pixelSize: parent.width / 8 
            font.weight: Font.Medium     // on the rectangle width, devided
            font.letterSpacing: 2        // by 8, spacing between letters and
            color: parent.color          // color of the text. Glow Type to
        }                                // glow text inside rectangle. Will
        Glow {                           // fill to the text size. Set radius 
            anchors.fill: txt1           // of the glow arround the text and
            radius: 7                    // samples property. Custom property
            samples: 17                  // to set the color of the text
            color: txglow                // from outside. Glow Type give a
            source: txt1                 // posibility to glow the texts, 
        }                                // objects, images, etc. This object 
    }                                    // with glow effect can be used as
}                                        // Button or other element.
