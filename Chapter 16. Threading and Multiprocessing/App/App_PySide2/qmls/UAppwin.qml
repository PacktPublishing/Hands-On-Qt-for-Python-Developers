import QtQuick 2.7                          // The Item and Rectangle.
import QtQuick.Controls 1.4                 // For the Window App.
import QtQuick.Controls.Styles 1.4          // For StatusBar styling.
import QtQuick.Window 2.2 as SZ             // For the Screen resolution.
import QtQuick.Layouts 1.3                  // StackLayout import.
import "bars" as Bars                       // Elements - Menu, ToolBars.
import "." as Qmls                          // Importing the qmls/ directory.
import "gradients" as SApp                  // Gradients for the StatusBar.

ApplicationWindow {                         // Window with width and height
    width: SZ.Screen.desktopAvailableWidth  / 2 
    height: SZ.Screen.desktopAvailableHeight / 2 
    title: "QML Application"                // for this device minus bars
    menuBar: Bars.MBar {}                   // and menus divided by 2.
    toolBar: Bars.TBar {}                   // TBar/MBar from the qmls/bars/.
    Bars.TaBar {                            // TabBar form the bars/.
        id: tabar1                          // Id of the TabBar will be used.
        width: parent.width                 // TabBar is equal to the width
    }                                       // of the application window.
    StackLayout {                           // Stack layout that will be used
        id: sl1                             // with TabBar to show the items.
        width: tabar1.width                 // Items related to the index of
        height: tabar1.height               // TabBar will be demonstrated.
        currentIndex: tabar1.currentIndex   // Element of the Layout that
        Qmls.UAppItems {                    // will shown item depends from 
            width: tabar1.width             // their index. Width and height 
            height: tabar1.height           // of the imported UItem that 
        }                                   // equal to the width and height
    }                                       // of layout, used with TabBar.
    statusBar: StatusBar {                  // Status bar for the app, that
        anchors.fill: parent                // filled as parent size with 
        Label { text: "Reading..."; color: "red" }
        style: StatusBarStyle {             // label and text. StatusBar 
            background: Rectangle {         // such as MenuBar and ToolBar
                anchors.fill: parent        // have a style property, that
                SApp.UGradientWin {}        // can be used by styling with 
            }                               // StatusBarStyle from the 
        }                                   // QtQuick.Controls.Styles, and 
    }                                       // for ApplicationWindow can be 
}                                           // used ApplicationWindowStyle.
