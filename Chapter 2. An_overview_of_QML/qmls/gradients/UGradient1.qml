import QtQuick 2.7

Gradient {                // Declare Gradient type.
    GradientStop {        // First GradientStop, position
        position: 0.0;    // of the start of the gradient,
        color: "red";     // and color to this position.
    }                     // GradientStop demonstrates where
    GradientStop {        // stoped the color gradient 
        position: 0.27;   // and started new color gradients. 
        color: "#AAFF00"; // In the Gradient type available 
    }                     // only vertical gradient, or from 
    GradientStop {        // top to bottom of the object.  
        position: 0.534;  // Position - is a real type number,
        color: Qt.rgba(0.95,0,0,1); // from 0 to 1 and can be  
    }                     // 0.7 or 0.777, that demonstrate  
    GradientStop {        // the gragient of the colors of 
        position: 0.7147; // this position color and color  
        color: "yellow";  // of the position before. If  
    }                     // available just two GradientStop
    GradientStop {        // positions as 0 and 1, the 
        position: 1.0;    // gradient color will consist
        color: Qt.rgba(1,0,0,1); // two colors. 
    }                     // Color of the last
}                         // position of the GradientStop.
