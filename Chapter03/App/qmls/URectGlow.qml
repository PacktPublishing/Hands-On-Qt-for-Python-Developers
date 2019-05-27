import QtQuick 2.7                            // Importing the Rectangle.
import QtGraphicalEffects 1.0                 // Importing RectangularGlow.

Rectangle {                                   // Box for glowing rectangle.
    property color glowcolor                  // Custom property, glow color.
    property color txglow                     // Property, text glow color.
    property string txtext                    // Custom property for text.
    property color txcolor                    // Property for text color.
    property real glowr: 10                   // Custom property for radius.
    property real spr: 0.1                    // Custom property for spread.
    property real whr: 1.5                    // Size of the elements.
    property real rdx: 14                     // Property for the radius.
    RectangularGlow {                         // RectangularGlow, must be 
        id: rglow                             // before the rectangle wich  
        anchors.fill: rectglow                // will glow to get the effect.
        glowRadius: parent.glowr              // Glow around element.
        spread: parent.spr                    // Spread, decreasing move
        color: glowcolor                      // to more distortion.
        cornerRadius: rectglow.radius + glowRadius 
    }                                         // Corner radius.
    Rectangle {                               // Rectangle, have a glow
        id: rectglow                          // with color similar to the
        color: parent.color                   // parent rectangle color.
        anchors.centerIn: parent              // Set to the center in the 
        width: parent.width / parent.whr      // parent with width and 
        height: parent.height / parent.whr    // height of parent / 1.5.
        radius: rdx                           // Set radius of the corners.
        Text {                                // Set text which will glow
            id: txt1                          // with Glow Type. Set text to
            anchors.centerIn: parent          // the center of the parent
            text: txtext                      // rectangle. Font family,
            font.family: "Helvetica"          // pixel size of the font
            font.pixelSize: parent.width / 8  // depends from the rectangle
            font.weight: Font.Medium          // width, devided by 8, spacing
            font.letterSpacing: 2             // between letters and color of
            color: txcolor                    // the text. Glow Type to glow
        }                                     // text inside rectangle. Will
        Glow {                                // fill to the text size. Set
            anchors.fill: txt1                // radius of the glow arround 
            radius: parent.radius / 2         // the text and samples
            samples: 17                       // property. Custom property to
            color: txglow                     // set the color of the text
            source: txt1                      // from outside. Glow Type give
        }                                     // a posibility to glow the
    }                                         // texts, objects, images, or
}                                             // any other related elements.
