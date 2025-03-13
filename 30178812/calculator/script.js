const screen = document.getElementById("screen");
const container = document.getElementById("container");
let sum = 0;

container.addEventListener("click", (event) => {
    let target = event.target;
    let element = target.id;
    console.log("Container event listener called")
    console.log(`Target: ${target} Element: ${element}`)
    if(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"].includes(element)) {
        addtoScreen({"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0}[element]);
    } else if(element == "addition") {
        addition();
    };
});


function addtoScreen(number) {
    screen.innerHTML += String(number);
};

function addition() {

};