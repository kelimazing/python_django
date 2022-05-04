var p1 = prompt("Please enter your name. Your color will be blue");
var p1color = "rgb(86, 151, 255)";

var p2 = prompt("Please enter your name. Your color will be red");
var p2color = "rgb(237, 45, 73)";

var grayColor = 'rgb(128, 128, 128)'
var table = $("table tr");

var tableRow = $("tr").length
var tableColumn = $("tr").eq(0).find("td").length

// Change Color
function changeColor(rowIndex, colIndex, color) {
    table.eq(rowIndex).find("td").eq(colIndex).find("button").css("background-color", color);
}

// Return what color is the button
function returnColor(rowIndex, colIndex) {
  return table.eq(rowIndex).find("td").eq(colIndex).find("button").css("background-color");
}


// Get Row index of the bottommost gray tile
function checkBottom(colIndex) {
  for (var i = 5; i > -1; i--) {
    if (returnColor(i, colIndex) === 'rgb(128, 128, 128)') {
      return i;
    }
  }
}

// Check for winner
// Check win
function isWin(one, two, three, four) {
  return (one === two && one === three && one === four && one !== 'rgb(128, 128, 128)' && one !== undefined);
}

// Win console
function reportWin(row, col) {
  console.log("Win on Col:" + (col + 1) + " Row:" + (row + 1));
}

// Horizontal win
function hWin() {
  for (var row = 0; row < tableRow; row++) {
    for (var col = 0; col < tableColumn - 3; col++) {
      if (isWin(returnColor(row, col), returnColor(row, col+1), returnColor(row, col+2), returnColor(row, col+3))) {
        reportWin(row, col);
        console.log("Horizontal Win");
        return true;
      }else {
        continue;
      }
    }
  }
}

// Vertical win
function vWin() {
  for (var col = 0; col < tableColumn; col++) {
    for (var row = 0; row < tableRow - 3; row++) {
      if (isWin(returnColor(row, col), returnColor(row+1, col), returnColor(row+2, col), returnColor(row+3, col))) {
        reportWin(row, col);
        console.log("Vertical Win");
        return true;
      }else {
        continue;
      }
    }
  }
}

// Diagonal win
function dWin() {
  for (var col = 0; col < tableColumn - 3; col++) {
    for (var row = 0; row < tableRow; row++) {
      if (isWin(returnColor(row, col), returnColor(row+1, col+1), returnColor(row+2, col+2), returnColor(row+3, col+3))) {
        reportWin(row, col);
        console.log("Diagonal Win");
        return true;
      }if (isWin(returnColor(row, col), returnColor(row-1, col+1), returnColor(row-2, col+2), returnColor(row-3, col+3))) {
        reportWin(row, col);
        console.log("Diagonal Win");
        return true;
      }else {
        continue;
      }
    }
  }
}

// Game over
function gameOver(winner) {
  $("h1").text(winner + " wins!");
  $("h2").text("You may now refresh the page to play again!");
  $("h3").fadeOut('fast');
  $("button").off('click');
}

// BEGIN GAME
// Initate player details
var currentPlayer = 1
var currentColor = p1color
var currentName = p1

// Start with player 1
$("h3").text(currentName + ": It's your turn to drop a blue chip!")

// Change color of bottommost gray on click
$("button").on('click', function() {
  // Get Column
  var col = $(this).closest("td").index();

  // Get Row
  var row = checkBottom(col);

  // Change color
  changeColor(row, col, currentColor);

  // Check if there is a winner
  if (hWin() || vWin() || dWin()) {
    gameOver(currentName);
  }

  // Change player per turn
  currentPlayer = currentPlayer * -1;
  if (currentPlayer === 1) {
    currentName = p1;
    currentColor = p1color;
    $("h3").text(currentName + ": It's your turn to drop a blue chip!")
  }else {
    currentName = p2;
    currentColor = p2color;
    $("h3").text(currentName + ": It's your turn to drop a red chip!")
  }
})
