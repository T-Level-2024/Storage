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

function updateTaskList() {
    list.innerHTML = "";
    console.log(tasks);
    let newbutton;
    for (let i=0; i<tasks.length; i++) {
        if(tasks[i][1]){
            list.innerHTML += `<li id="L${i}"><input id="L${i}I" type="text" placeholder="New text here"><button id="L${i}S">Submit</button><button id="L${i}R">Remove</button></li>`;
        } else {
            list.innerHTML += `<li id="L${i}">${tasks[i][0]} <button id="L${i}E">Edit</button><button id="L${i}R">Remove</button></li>`;
            newbutton = document.getElementById(`L${i}E`);
            newbutton.addEventListener("click", () => enableEditing(Number(`${i}`)));
        }
        newbutton = document.getElementById(`L${i}R`);
        newbutton.addEventListener("click", () => removeItem(Number(`${i}`)));
    };
};

function enableEditing(element) {
    tasks[element][1] = true;
    updateTaskList();
}

function replaceItem(element, text) {
}

function removeItem(element) {
    tasks.pop(element);
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