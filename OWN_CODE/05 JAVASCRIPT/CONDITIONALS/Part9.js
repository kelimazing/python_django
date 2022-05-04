var fn = prompt("First name:")

var ln = prompt("Last name:")

var age = prompt("Age:")

var height = prompt("Height (cm):")

var pet = prompt("Pet Name:")

alert("Thank you!")

if (fn[0] == ln[0] && age >= 20 && age <= 30 && height >= 170 && pet[(pet.length) - 1] == 'y') {
  console.log("Congratulations Agent!");
}

else {
  console.log("Nothing to see here bud.");
}
