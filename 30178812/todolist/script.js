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

list.addEventListener("click", (event) => {
    // Checks what the element ID ends with:
    // R for remove
    // E for edit
    // S for submit (comes up after edit is pressed)
    let target = event.target;
    let element = target.id;
    let index = element.charAt(1);
    if (element.endsWith("R")) {
        removeItem(index);
    } else if (element.endsWith("E")) {
        enableEditing(index);
    } else if (element.endsWith("S")) {
        replaceItem(index, document.getElementById(`L${index}I`).value);
    }
})

function updateTaskList() {
    list.innerHTML = "";
    console.log(tasks);
    let index;
    for (let i=0; i<tasks.length; i++) {
        index = i;
        console.log(`updateTaskList(): I(${index}) task(${tasks[index]})`);
        if(tasks[i][1]){ 
            // Input box, submit, remove
            // Any existing text is moved to the input box.
            list.innerHTML += `<li id="L${index}"><input id="L${index}I" type="text" placeholder="New text here" value="${tasks[index][0]}"><button id="L${index}S">Submit</button><button id="L${index}R">Remove</button></li>`;
        } else { 
            // Item, edit, remove
            // User can either edit the item text or remove the item entirely
            list.innerHTML += `<li id="L${i}">${tasks[index][0]} <button id="L${index}E">Edit</button><button id="L${index}R">Remove</button></li>`;
        };
    };
};

function enableEditing(element) {
    tasks[element][1] = true;
    updateTaskList();
}

// submit button functiojn
// print to the console 

function replaceItem(element, text) {
    console.log(`L${element}: ${tasks[element][0]} --> ${text}`);
    tasks[element][0] = text;
    tasks[element][1] = false;
    updateTaskList();
}

function removeItem(element) {
    tasks.splice(element, 1);
    updateTaskList();
}

addbutton.addEventListener("click", () => {
    tasks.push([input.value, false]);
    input.value = "";
    updateTaskList();
});

removebutton.addEventListener("click", () => {
    //list.removeChild(list.lastElementChild);
    list.innerHTML = ""
    tasks = [];
});