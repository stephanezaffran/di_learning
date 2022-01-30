// Exercise 1 : Move The Box
// Instructions
// Move the box from left to right
// Tip: use setInterval



// dan exercice 

// // create global var to target the red
// let redbox = document.querySelector("#animate")
// let interval
// // create a fonction that move 50px left and 50 px top for red
// let topValue  = 0
// let movIt = () => {
//     console.log("hello")
//     topValue = isNaN(parseInt(redbox.style.top))
//         ? 0
//         :parseInt(redbox.style.left)
//         topValue += 50
//     if (topValue <= 350) {
//         redbox.style.top = `${topValue}px`
//         redbox.style.left = `${topValue}px`
//     }else{
//         clearInterval(interval)
//     }
// }
// //stop the interval a the good moment
// let myMove = () => {
//     if(topValue===400){
//         interval = undefined
//         redbox.style.top = `0px`
//         redbox.style.left = `0px`
//     }
//     //create a setinterval for the function
//     if(!interval){interval = setInterval(movIt, 250)}
//     // setInterval(movIt, 1000)
// }
// //an ebent listener on butoon click

function myMove() {
    var elem = document.getElementById("animate");
    var position = 0;
    var id = setInterval(() => {

        if (position == 350) {
            clearInterval(id);
        }
        position++;
        elem.style.left = `${position}px`;
    }, 10);

}


//Exercise 2: Drag & Drop
// Instructions
// Tip : Check out this video on drag and drop


let element = document.querySelector("#box")
element.setAttribute('draggable', 'true');

element.addEventListener("dragstart", function(event) {
    event.target.style.backgroundColor = "lightpink";
    console.log("drag " + "X: " + event.clientX + " Y: " + event.clientY);
});

element.addEventListener("dragend", function(event) {
    event.target.style.backgroundColor = "red";
    let _x = event.clientX;
    console.log(_x)
    let _y = event.clientY;
    console.log(_y)
    console.log(event)
    event.target.style.left = _x - 25 + "px";
    event.target.style.top = _y - 75 + "px";
    //event.target.style.position = "absolute"; //Necessary
    console.log("dragend" + "X: " + event.clientX + " Y: " + event.clientY);
});


// Create a draggable square/box element in your HTML file.
// In your javascript file add the functionality which will allow you to drag the 
// square/box and drop it into a larger box.