import QtQuick 2.7                          // ListView, ListElement imports.
import QtQuick.Controls 1.4                 // TableView, TableViewColumn.
import QtQuick.Controls.Styles 1.4          // TableViewStyle importing.
import QtQuick.Layouts 1.3                  // Layouts importing.

GridLayout {                                // Simple example of the table
    TableView {                             // with GUI application creation.
        Layout.fillWidth: true; Layout.fillHeight: true;
        Layout.margins: 20                  // Set margins all around sides.
        TableViewColumn {                   // Table view and columns with
            horizontalAlignment: Text.AlignHCenter
            role: "num1"; title: "Title 1"  // title and role for each column     
        }                                   // in the table. Title will be as
        TableViewColumn {                   // name for column and role will
            horizontalAlignment: Text.AlignHCenter
            role: "num2"; title: "Title 2"  // bound the elements of each               
        }                                   // cell. Horizontal Alignment
        TableViewColumn {                   // and style provides the center
            horizontalAlignment: Text.AlignHCenter
            role: "num3"; title: "Title 3"  // align and color of the text.           
        }                                   // ListModel that added to the
        style: TableViewStyle {textColor: "red"}
        model: ListModel {                  // model property for this
            id: lm1                         // TableView that will provide
            ListElement {num1: "1_1"; num2: "1_2"; num3: "1_3"}
            ListElement {num1: "2_1"; num2: "2_2"; num3: "2_3"}
            ListElement {num1: "3_1"; num2: "3_2"; num3: "3_3"}
        }                                   // the elements for each cell in
    }                                       // the table. ListModel Type used
}                                           // to create the table model.  