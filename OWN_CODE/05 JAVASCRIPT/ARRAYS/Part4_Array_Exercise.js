// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew() {
  var name = prompt("Please enter the name you wish to add: ");
  roster.push(name);

}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster
function deleteName() {
  var name = prompt("Please enter the name you wish to remove");
  var index = roster.indexOf(name);
  if (index > -1) {
    roster.splice(index, 1);
  };
}
// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function displayRoster() {
  console.log(roster)
}

// Start by asking if they want to use the web app
var q = prompt("Would you like to start the web app? (y/n)")
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
if (q === "y") {
  while (true) {
    var action = prompt("What action do you want to do? (add, remove, display, or quit)")
    if (action === "add") {
      addNew();
    }
    else if (action === "remove") {
      deleteName();
    }
    else if (action === "display") {
      displayRoster()
    }
    else if (action === "quit") {
      break;
    }
  }
}
