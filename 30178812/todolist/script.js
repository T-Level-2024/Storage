const list = document.getElementById("list");
const input = document.getElementById("input");
const addbutton = document.getElementById("add");
const removebutton = document.getElementById("remove");


addbutton.addEventListener("click", () => {
    //list.innerHTML += `<li>${input.value}</li>`
    list.innerHTML += `<li id="${input.value}">${input.value} <button onClick="document.getElementById('list').removeChild(document.getElementById('${input.value}'))">Remove</button></li>`;
});

removebutton.addEventListener("click", () => {
    //list.removeChild(list.lastElementChild);
    list.innerHTML = ""
});