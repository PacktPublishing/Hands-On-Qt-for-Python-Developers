import QtQuick 2.7                         // Import for the Item.

Item {                                     // Parent Item of the all items.
    id: main_item                          // Set id of the main item.
    anchors.fill: parent                   // Set parent`s width and height.
    anchors.margins: 20                    // Set margins between Items.      
    Item {                                 // First item, child of the item.
        id: i1                             // Set id of the first item.
        x: 50                              // 50 px from the left side.
        width: parent.width / 2            // Parent`s width divided by 2.
    	height: parent.height / 4          // Parent`s width divided by 4.
        z: 1                               // Will cover item with id: i3.
        opacity: 0.5                       // Half opaque opacity.
        Rectangle {                        // Red Rectangle.
            id: r1                         // Set id of the red rectangle.
            width: parent.width            // Set width as parent item - i1.
            height: parent.height          // Height as parent item - i1.
            color: "#FF0000"               // Color red.
            MouseArea {                    // Area of the red rectangle.
                anchors.fill: parent       // Area to width of the parent.
                onClicked: {i1.state == 'state1' ?
                            i1.state = '' : i1.state = 'state1'}
            }                              // If clicked, red will move.
        }                                  // Inherits Item type properties.
        states: [                          // Set states to Item - id i1.
            State {                        // State Type, state for the item
                name: "state1"             // with name that signed with
                PropertyChanges { target: i1; x: 140 } 
            }                              // onClicked, PropertyChanges with
        ]                                  // target id and x property.
        transitions: [                     // Transitions for the all state
            Transition {                   // changes with Transition Type,
                NumberAnimation { properties: "x, y" }
            }                              // animation of the x and y
        ]                                  // properties by default depends
	}                                      // from state changes.
	Item {                                 // Second item, child item i1.
    	id: i2                             // Set id of the second item.
    	parent: i1                         // Set parent of the item.
    	y: i1.height                       // Set item to position.
        width: parent.width / 2            // Width same as width of i1 / 2.
    	height: parent.height / 4          // Height same as i1 / 4.
    	scale: 2                           // Size at 2 times more than i1.
    	z: 2                               // Covered by i1 and cover i3.
    	opacity: 0.7                       // Item will more opaque than i1. 
        Rectangle {                        // Green Rectangle.
            id: r2                         // Id of the rectangle.                
            width: parent.width            // Set width same as parent i2.
            height: parent.height          // Set height same as parent i2.
            color: "#00FF00"               // Color green.
            MouseArea {                    // Area for the green rectangle.
                anchors.fill: parent       // Area to width of the parent.
                onClicked: {parent.y == 140 ?
                            parent.y = 270 : parent.y = 140}
            }                              // Green rectangle will move.
            Behavior on y {                // Set the y-axis that will
                NumberAnimation {          // use animation of the fall down
                    duration: 7000         // of the green rectangle with
                    easing.type: Easing.OutInElastic  
                }                          // duration as 7 seconds and
            }                              // Type of easing curve as 
        }                                  // elastic (exponentially decaying 
	}                                      // sine wave).
	Item {                                 // Third item, child of the item.
    	id: i3                             // Set id of the third item.
    	anchors.centerIn: parent           // Set by the center to main_item.
    	y: i1.height + i2.height           // Set to where item 2 is ending. 
        width: parent.width / 2            // Width as main_item / 2.
    	height: parent.height / 4          // Height as main_item / 4.
    	rotation: 90                       // Item rotated on 90 degrees.
    	z: 0                               // Covered by i1 and 12, cover i4.
    	opacity: 0.9                       // Item will be almost opaque. 
        Rectangle {                        // Yellow Rectangle, child item. 
            id: r3                         // Id of the third rectangle.
            width: parent.width            // Width same as i3 item.
            height: parent.height          // Height same as i3 item.
            color: "#FFFF00"               // Color yellow.
            SequentialAnimation on x {     // The yellow rectangle will 
                id: sa1                    // animated one after the other.
                running: false             // Set running to false.
                loops: Animation.Infinite  // Loops will infinte.
                NumberAnimation {          // Rectangle will be animated with
                    from: 140              // drop down by y axis property
                    to: 270                // to the 270 position and
                    duration: 7000         // with duration of 0.7 seconds.
                    easing.type: Easing.OutInElastic 
                }                          // Accelerated after halfway.
                NumberAnimation {          // Rectangle will be animated 
                    from: 270              // with rising up from bottom
                    to: 140                // to top to position of y axis
                    duration: 7000         // as 140 with similar duration.
                    easing.type: Easing.OutInElastic
                }                          // Easing type the same as above.
                PauseAnimation { duration: 1400 }  
            }                              // Set pause between loops of the
            MouseArea {                    // animation. Mouse Area for the
                anchors.fill: parent       // yellow rectangle. Area to width
                onClicked: sa1.running = true 
            }                              // of the parent. Rinning
        }                                  // animation. If clicked, yellow
	}                                      // rectangle will move.
	Item {                                 // Fourth item, child of r3.
    	id: i4                             // Set id of the fourth item.
    	parent: r3                         // Set parent with id r3.
        width: parent.width                // As rectangle r3 width.
    	height: parent.height              // Height as rectangle r3 width.
    	z: 1                               // Will cover rectangle r3.
    	rotation: 45                       // Will be rotated on 45 degrees. 
    	scale: 0.7                         // Will be less than rectangle 3.
        Rectangle {                        // Violet Rectangle, child item. 
            id: r4                         // Id of the fourth rectangle.
            anchors.centerIn: parent       // Set by the center to i4.
            width: parent.width            // Width same as r3 item * 0.7.
            height: parent.height          // Height same as i3 item * 0.7.
            antialiasing: true             // Set antialiasing.
            color: "#770077"               // Color violet.
            ParallelAnimation {            // The violet rectangle will 
                id: sa2                    // animated at the same time.
                running: false             // Set running to false.
                loops: Animation.Infinite  // Loops will infinte.
                PropertyAnimation {        // Rectangle will be animated with
                    target: r4             // Set rectangle id that will be 
                    property: "rotation"   // animated with rotation.
                    from: 0                // Rotation of the rectangle from
                    to: 360                // to the 360 degrees
                    duration: 7000         // with duration of 7 seconds.
                    easing.type: Easing.OutInElastic  
                }                          // Accelerated after halfway.
                PropertyAnimation {        // Red rectangle with id r1 
                    target: r1             // will be animated with
                    property: "rotation"   // rotation property at the
                    from: 0                // same time as will animated
                    to: 360                // violet rectangle with id r4.
                    duration: 7000         // Duration as 7 seconds.
                    easing.type: Easing.InQuart  
                }                          // Will be accelerating from zero
            }                              // velocity. Easing curve for a
            MouseArea {                    // quartic function. Mouse Area
                anchors.fill: parent       // for the yellow rectangle. Area
                onClicked: sa2.running = true 
            }                              // to width of the parent. Running
        }                                  // animation. If MouseArea will
	}                                      // clicked, yellow rectangle
}                                          // will move.