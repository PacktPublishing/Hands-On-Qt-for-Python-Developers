import QtQuick 2.7                            // Importing the Item.
import QtQuick.Controls 2.2                   // TabBar and TabButton import.

TabBar {                                      // TabBar is used for
    anchors.fill: parent                      // implementing different views                   
     Repeater {                               // in the app with ability to  
         model: ["Actions", "Views", "Models"]
         TabButton {                          // switch between these views.
            text: modelData                   // Tab Bar can be styled with             
        }                                     // background and contentItem 
    }                                         // properties and TabButton can
}                                             // be styled similar to Button.