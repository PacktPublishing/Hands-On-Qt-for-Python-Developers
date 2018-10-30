import QtQuick 2.7             // For Rectangle.
import QtGraphicalEffects 1.0  // For RectangularGlow.

Rectangle {          // Parent box for the glowing rectangle.
    property color glowcolor // Custom property, glow color.
    property color txglow// Custom property, text glow color.
    RectangularGlow { // RectangularGlow object, must to be 
        id: rglow     // placed before of the rectangle wich  
        anchors.fill: rectglow// will glow to get the effect.
        glowRadius: 10// Radius of the glow around element.
        spread: 0.1   // Spread of the glow, decreasing move
        color: glowcolor // to more distortion of the color.
        cornerRadius: rectglow.radius + glowRadius // Corner
    } // radius of the glow, equal to the object and glow.
    Rectangle { // Center rectangle, which will have a glow
        id: rectglow     // effect with color similar to the 
        color: parent.color      // parent rectangle color.
        anchors.centerIn: parent // Set to the center in the 
        width: parent.width / 1.5  // parent with width and 
        height: parent.height / 1.5// height of parent / 1.5.
        radius: 14   // Set radius of the rectangle corners.
        Text {    // Set text into rectangle which will glow
            id: txt1 // such as rectangle but with Glow Type.
            anchors.centerIn: parent // Set text to the
            text: "PUSH"  // center of the parent rectangle.
            font.family: "Helvetica" // Font family, pixel
            font.pixelSize: parent.width / 8 // size of the
            font.weight: Font.Medium // font depends from 
            font.letterSpacing: 2  // the rectangle width,
            color: parent.color // devided by 8, spacing
        }  // between letters and color of the text.
        Glow { // Glow Type to glow text inside rectangle.
            anchors.fill: txt1// Will fill to the text size.
            radius: 7 // Set radius of the glow arround the
            samples: 17       // text and samples property.
            color: txglow // Custom property to set the 
            source: txt1  // color of the text from outside.
        } // Glow Type give a posibility to glow the texts,
    }     // objects, images, etc. This object with glow 
}         // effect can be used as Button or other element.
