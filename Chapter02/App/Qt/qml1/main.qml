import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 350
    height: 590
    title: qsTr("First QML")
    Rectangle {  // You script here.
        anchors.centerIn: parent
        width: parent.width / 2
        height: parent.height / 2
        color: "red"
    }
}
