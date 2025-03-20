const data = {"T1":"Class Time",
    "T2":"Class Name",
    "T3":"Available Places",
    
    "C1":"9:00 AM",
    "C2":"Yoga",
    "C3":"4",

    "C4":"10:30 AM",
    "C5":"Pilates",
    "C6":"3",

    "C7":"12:00 PM",
    "C8":"Spin Class",
    "C9":"7"}
let element;
for (let i=0;i<3;i++){
    element = document.getElementById(`T${(i+1)}`);
    element.innerText = data[`T${(i+1)}`];
};
for (let i=0;i<9;i++){
    element = document.getElementById(`C${(i+1)}`);
    element.innerText = data[`C${(i+1)}`];
}