console.log("Connected");

// Get tiles
var tiles = document.querySelectorAll("td")

// Change a box
function changeBox() {
  if (this.textContent === "") {
    this.textContent = "X";
  }else if (this.textContent === "X") {
    this.textContent = "O";
  }else {
    this.textContent = "";
  }
}

// Restart
var restart = document.getElementById('b')
restart.addEventListener("click", function() {
  for (var i = 0; i < tiles.length; i++) {
    tiles[i].textContent = "";
  }
})

// Implement changeBox to all box
for (var i = 0; i < tiles.length; i++) {
  tiles[i].addEventListener("click", changeBox)
}
