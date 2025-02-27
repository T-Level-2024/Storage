import { pi } from "./utils.js";
console.log(pi);
console.log("This is working.");
let message = "Hello, Javascript";
const author = "Author";
var count = 0;

let num1 = 10;
let num2 = 5;
let sum = num1 + num2;
let diff = num1 - num2;
let product = num1 * num2;
let quotient = num1 / num2;
let remainder = num1 % num2;

console.log("Num1: "+num1, "Num2: "+num2, "Sum: "+sum, "Diff: "+diff, "Product: "+product, "Quotient: "+quotient, "Remainder: "+remainder);



const fruits = ["Apple", "Banana", "Mango", "Orange"];
console.log("Loops output:");
fruits.map((fruit => console.log(fruit)));

let age = 18
if(age >= 18) {
    console.log("You are allowed to drink.");
} else if(age < 18) {
    console.log("Have milk");
} else {
    console.log("Stick to diet coke.");
};

let day = "Monday";
switch(day){
    case "Monday":
        console.log("Get up for work");
        break;
    case "Sunday":
        console.log("Relax");
        break;
    default:
        console.log("Work");
        break;
};

const mybutton = document.getElementById("mybutton");
const input = document.getElementById("textinput");
const output = document.getElementById("paragraph");
mybutton.addEventListener("click",() => {
    //mybutton.innerText = input.value;
    let name = input.value
    if(name){
        //console.log(`Hello, $(input.value)`)
        output.innerText = `Hello, ${name}`
    }
})