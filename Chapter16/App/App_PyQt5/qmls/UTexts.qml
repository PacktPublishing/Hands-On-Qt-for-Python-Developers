import QtQuick 2.7                             // Rectangle, MouseArea, etc.
import QtQuick.Layouts 1.3                     // Layout importing.
import QtQuick.Controls 1.4                    // Controls elements.
import QtQuick.Controls.Styles 1.4             // Styling of the controls.
import QtQuick.Dialogs 1.2                     // Font, Color dialogs.

GridLayout {                                   // The most usefull elements
    TextArea {                                 // from the controls submodule
        id: ta1; Layout.column: 0; Layout.rowSpan: 5; Layout.columnSpan: 3
        Layout.fillWidth: true; Layout.fillHeight: true
        Layout.minimumWidth: parent.width / 2  // that can be implemented
        font.pixelSize: sl1.value; textColor: "lightgrey"; textMargin: 10
    }                                          // with GUI. Calendar Type
    Calendar {                                 // that provides the simple
        id: cd1; Layout.row: 0; Layout.column: 3; Layout.columnSpan: 2
        Layout.fillWidth: true; Layout.fillHeight: true
    }                                          // calendar widget in the app.
    Slider {                                   // Slider will increase or
        id: sl1; Layout.row: 1; Layout.column: 3
        Layout.fillWidth: true; Layout.fillHeight: true
        Layout.maximumHeight: parent.height / 24
        updateValueWhileDragging: true         // decrease the text size
        minimumValue: 0; maximumValue: 100; value: 19
    }                                          // inside text area. Combo box
    ComboBox {                                 // that provide an option to
        id: cb1; Layout.row: 1; Layout.column: 4          
        Layout.fillWidth: true; Layout.fillHeight: true
        Layout.maximumHeight: parent.height / 24
        model: ["Dialogs", "Change Font", "Change Color"]
        currentIndex: 0                        // choose the Font and Color
        onCurrentIndexChanged: {               // for the text of the text
            if (currentText=="Change Font") {  // area with open dialog
                fontd1.open(); cb1.currentIndex = 0;};
            if (currentText=="Change Color") { // windows of the font and
                colord1.open(); cb1.currentIndex = 0;};
        }                                      // color. These dialogs has a 
        FontDialog {                           // onAccepted handler to make
            id: fontd1                         // accept the choice of the
            onAccepted: {                      // font or color. If dialog
                ta1.font = fontd1.currentFont; fontd1.visible = false;
            }                                  // will canceled without any
            onRejected: fontd1.visible = false;
        }                                      // choice - dialog will closed
        ColorDialog {                          // and color with font of the
            id: colord1                        // text will not changed. To
            onAccepted: {                      // the cancel of the dialogs
                ta1.textColor = colord1.currentColor; colord1.visible = false;
            }                                  // is related a onRejected
            onRejected: colord1.visible = false;
        }                                      // handler. These dialogs are
    }                                          // static in the QtQuick.
    ExclusiveGroup { id: exgr }                // Also available open/save
    GridLayout {                               // file dialogs, etc.
        columns: 1; Layout.row: 2; Layout.column: 3; Layout.rowSpan: 2
        Repeater {                             // Using exclusive group
            id: rbrep1; model: ["1 line of the text", "1000 lines of the text"]
            RadioButton {                      // for radio buttons that
                exclusiveGroup: exgr;          // allows to choose just one
                Layout.fillWidth: true; Layout.fillHeight: true
                style: RadioButtonStyle {      // option from two available -
                    background: Rectangle {color: "#000F1F"}
                    label: Text {              // demonstrates RadioButton
                        text: modelData; color: "lightgray"
                        font.pixelSize: 14; font.letterSpacing: 2 
                    }                          // Type functionality. And
                }                              // styling of the buttons with
            }                                  // RadioButtonStyle type.
            Component.onCompleted: rbrep1.itemAt(0).checked = true;
        }                                      // onCompleted handler of the
    }                                          // Component Type provides the
    GridLayout {                               // check state of the radio
        columns: 1; Layout.row: 2; Layout.column: 4; Layout.rowSpan: 2
        Repeater {                             // buttons at the start of the
            id: rbrep2; model: ["Month number", "Milliseconds", "Scidate"]
            CheckBox {                         // application and default
                Layout.fillWidth: true; Layout.fillHeight: true
                style: CheckBoxStyle {         // choice. Check boxes with
                    background: Rectangle {color: "#000F1F"}
                    label: Text {              // abbility to use additional
                        text: modelData; color: "lightgray"
                        font.pixelSize: 14; font.letterSpacing: 2
                    }                          // functions to set the text
                }                              // in the text area. Will be
            }                                  // set the different variation
        }                                      // of the date and will be
    }                                          // included or excluded with
    TextField {                                // adding to the text area
        id: tf1; Layout.row: 4; Layout.column: 3
        Layout.fillWidth: true; Layout.fillHeight: true
        Layout.maximumHeight: rx1.height       // field. The Repeater Type
        horizontalAlignment: TextInput.AlignHCenter
        font.pixelSize: rx1.height / 2         // repeat the check boxes
        style: TextFieldStyle {background: Rectangle {radius: 7}}
    }                                          // creation without writing
    Rectangle {                                // these boxes in the code.
        id: rx1; Layout.row: 4; Layout.column: 4;
        Layout.fillWidth: true; Layout.fillHeight: true
        Layout.maximumHeight: cb1.height * 2   // Text Field provides the
        radius: 14; color: Qt.rgba(0.2, 0.2, 0.2, 1);
        Text {                                 // count of characters of the
            id: rtxt1; anchors.centerIn: parent; visible: true
            text: "Ok"; color: "green"; font.pixelSize: parent.width / 8
        }                                      // typed text. Usage of the
        BusyIndicator {id: bi1; anchors.centerIn: parent; running: false}
        Timer {                                // Rectangle instead the
            id: t1; interval: 300; running: false; repeat: false
            onTriggered: rx1.txdate();         // button, and adding of the
        }                                      // busy indicator that will
        function txdate() {                    // occurr when the rectangle
            var sd = cd1.selectedDate; var dateform = sd;
            if (rbrep2.itemAt(0).checked==true) {
                dateform = dateform + ", month-" + (cd1.visibleMonth + 1);
            } else {dateform = dateform};      // is clicked and will show
            if (rbrep2.itemAt(1).checked==true) {
                dateform = dateform + ", milliseconds: " + Date.parse(sd)
            } else {dateform = dateform};      // the operation process. To
            if (rbrep2.itemAt(2).checked==true) {
                var sdy = sd.getFullYear().toString();
                var sdmi = sd.getMonth() + 1; var sdm = sdmi.toString();
                var sdd = sd.getDate().toString();
                var sdh = sd.getHours().toString();
                var sdmt = sd.getMinutes().toString();
                var sds = sd.getSeconds().toString();
                var scid = sdy + sdm + sdd + sdh + sdmt + sds;
                dateform = dateform + ", scidate: " + scid;
            } else {dateform = dateform};      // implement the text with
            if (rbrep1.itemAt(0).checked==true) {
                ta1.text = dateform; tf1.text = ta1.length;
                bi1.running = false; rtxt1.text = "Ok"
            };                                 // date used the JS code and
            if (rbrep1.itemAt(1).checked==true) {
                for (var i = 0; i<1000; i++) { // JS date available
                    ta1.append(dateform);      // properties. Using of the JS
                    if (i==999) {              // Date object to manipulate
                        tf1.text = ta1.length; bi1.running = false; rtxt1.text = "Ok";
                    };                         // with date in the app. Call
                }                              // the items from the repeater
            };                                 // by position without id. For
        }                                      // loop of javascript will add
        MouseArea {                            // text lines to the text area
            anchors.fill: parent; hoverEnabled: true
            onEntered: {                       // so many times as signed, in
                rx1.color = Qt.rgba(0.25, 0.25, 0.25, 1); rtxt1.color = "lightgreen";
            }                                  // this case while not acheive
            onExited: {rx1.color = Qt.rgba(0.2, 0.2, 0.2, 1); rtxt1.color = "green";}
            onClicked: {rtxt1.text = ""; bi1.running = true; t1.running = true;}
        }                                      // to 1000. Timer Type allows
    }                                          // to set inerval between
}                                              // starting of the indicator.