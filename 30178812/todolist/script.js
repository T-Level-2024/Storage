const list = document.getElementById("list");
const input = document.getElementById("input");
const addbutton = document.getElementById("add");
const removebutton = document.getElementById("remove");
let tasks = [];

// tasks array
// new task is aded to this array
// you through this array, then for loop to make li elements for each task
// you can make an edit feature
// you can go through css
// deploy this

// make a function calle updateTaskList()

function removeEventListeners() {
    let element;
    for (let i = 0; i<tasks.length; i++) {
        element = document.getElementById(`L${i}R`);
        if(element) {
            element.replaceWith(element.cloneNode(true));
            console.log(`Replaced L${i}R`)
        }
    }
}

function updateTaskList() {
    if (list.innerHTML !== "") {
        removeEventListeners()
        list.innerHTML = "";
    }
    console.log(tasks);
    let newbutton;
    let index;
    for (let i=0; i<tasks.length; i++) {
        index = i;
        console.log(`updateTaskList(): I(${index}) task(${tasks[index]})`);
        if(tasks[i][1]){ // Input box, submit, remove
            list.innerHTML += `<li id="L${index}"><input id="L${index}I" type="text" placeholder="New text here"><button id="L${index}S">Submit</button><button id="L${index}R">Remove</button></li>`;
            newbutton = document.getElementById(`L${index}S`);
            setInterval(50);
            console.log(newbutton);
            newbutton.addEventListener("click", () => replaceItem(Number(`${index}`), document.getElementById(`L${index}I`).value));
            console.log("updateTaskList(): Submit event listener applied");
        } else { // Item, edit, remove
            list.innerHTML += `<li id="L${i}">${tasks[index][0]} <button id="L${index}E">Edit</button><button id="L${index}R">Remove</button></li>`;
            newbutton = document.getElementById(`L${index}E`);
            setInterval(50);
            console.log(newbutton);
            newbutton.addEventListener("click", () => enableEditing(Number(`${index}`)));
            console.log("updateTaskList(): Edit event listener applied");
        };
        newbutton = document.getElementById(`L${index}R`);
        setInterval(50);
        console.log(newbutton);
        newbutton.addEventListener("click", () => removeItem(Number(`${index}`)));
        console.log("updateTaskList(): Remove event listener applied");
    };
};

function enableEditing(element) {
    tasks[element][1] = true;
    updateTaskList();
}

// submit button functiojn
// print to the console 

function replaceItem(element, text) {
    console.log(`L${element}: ${text}`);
    tasks[element][0] = text;
    tasks[element][1] = false;
    updateTaskList();
}

function removeItem(element) {
    console.log("removeItem() called");
    tasks.splice(element, 1);
    updateTaskList();
}

addbutton.addEventListener("click", () => {
    tasks.push([input.value, false]);
    updateTaskList();
});










//addbutton.addEventListener("click", () => {
//    //list.innerHTML += `<li>${input.value}</li>`
//    list.innerHTML += `<li id="${input.value}">${input.value} <button onClick="document.getElementById('list').removeChild(document.getElementById('${input.value}'))">Remove</button></li>`;
//});
//
removebutton.addEventListener("click", () => {
    //list.removeChild(list.lastElementChild);
    list.innerHTML = ""
    tasks = [];
});