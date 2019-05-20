import QtQuick 2.7                                // Animations importing.
import QtQuick.Controls 1.4                       // Button import.
import QtQuick.Controls.Styles 1.4                // ButtonStyle import.
import "." as Qmls                                // URectGlow importing.

Button {                                          // Standard Button Type.
    property color bcolor: Qt.rgba(0, 0.07, 0.14, 1);
    property color gcolor: Qt.rgba(0.95, 0, 0, 1);
    property color tgcolor: Qt.rgba(0.77, 0, 0, 1);
    property color tcolor: Qt.rgba(0.2, 0.2, 0.2, 1);
    property real glrd: 3                         // Creation of the custom
    property real sprd: 0.5                       // props for using outside.
    property string btext                         // Implementing button text
    style: ButtonStyle {                          // in the parent object.
        background: Qmls.URectGlow {              // Styling of the standard
            id: but1                              // button with URectGlow
            txtext: btext                         // and ButtonStyle Type
            txcolor: tcolor                       // with background as has
            color: bcolor                         // URectGlow. Properties
            glowcolor: gcolor                     // of the URectGlow will be
            txglow: tgcolor                       // rewrited from outside
            glowr: glrd                           // settings such glows and 
            spr: sprd                             // texts, colors, radius,
            whr: 1.2                              // width/height relations,
            rdx: 7                                // spread of glow, etc. 
        }                                         // In counterweight to
    }                                             // Button Type can be used
}                                                 // Rectangle Type.
