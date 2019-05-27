import QtQuick.Controls 1.4                    // For the MenuBar Type.

MenuBar {                                      // Menu bar of the 
    Menu {                                     // application window, 
        title: "File"                          // consists Menu Types that
        MenuItem { text: "New" }               // represented with menu
        MenuItem { text: "Open" }              // bar. Each Menu with title
        MenuItem { text: "Save" }              // consist the Menu Items so
        MenuItem { text: "Save as" }           // many as needed, number of
    }                                          // the Menu limited just with
    Menu {                                     // width of the application
        title: "Edit"                          // window and number of the
        MenuItem { text: "Cut" }               // MenuItems just with height. 
        MenuItem { text: "Copy" }              // For styling of the MenuBar
        MenuItem { text: "Paste" }             // is used a MenuBarStyle
    }                                          // Type of the
    Menu {                                     // QtQuick.Controls.Styles 1.4 
        title: "Tools"                         // and for styling of the Menu 
        MenuItem { text: "Tool # 1" }          // Type is used the MenuStyle
        MenuItem { text: "Tool # 2" }          // object. Styling can be used
        MenuItem { text: "Tool # 3" }          // with properties and rules
    }                                          // that are signed in the 
}                                              // official documentation.