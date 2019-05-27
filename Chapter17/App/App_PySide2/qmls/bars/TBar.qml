import QtQuick 2.7                            // Importing the Item.
import QtQuick.Controls 1.4                   // Importing the ToolBar Type.
import QtQuick.Layouts 1.2                    // Importing the RowLayout.

ToolBar {                                     // Tool bar for the application
    RowLayout {                               // window. Tool buttons are
        anchors.fill: parent                  // aligned with RowLayout Type
        ToolButton {                          // from the QtQuick.Layouts
            iconSource: "Icons/python1.png"   // module. ToolButton is used
        }                                     // to implementing some useful
        ToolButton {                          // toolset in the application.
            iconSource: "Icons/python2.png"   // ToolBar can be styled with
        }                                     // ToolBarStyle Type that
        ToolButton {                          // available with importing of
            iconSource: "Icons/Aiconda.png"   // the QtQuick.Controls.Styles
        }                                     // and tool buttons can be
        Item { Layout.fillWidth: true }       // styled with ButtonStyle.
    }                                         // The item is used to fill
}                                             // the empty space of the bar.