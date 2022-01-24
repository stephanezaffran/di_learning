// Copy the code below, into a structured HTML file:

// <article>
//     <h1> Some Facts </h1>
//     <h2> The Chocolate </h2>
//     <h3> History of the chocolate </h3>
//     <p> Chocolate is made from tropical Theobroma cacao tree seeds. 
//     Its earliest use dates back to the Olmec civilization in Mesoamerica.</p>
//     <p> After the European discovery of the Americas, chocolate became 
//     very popular in the wider world, and its demand exploded. </p>
//     <p> Chocolate has since become a popular food product that millions enjoy every day, 
//     thanks to its unique, rich, and sweet taste.</p> 
//     <p> But what effect does eating chocolate have on our health?</p> 
// </article>


// Using a DOM property, retrieve the h1 and console.log it.
console.log( document.querySelector('h1').textContent)

// Using DOM methods, remove the last paragraph in the <article> tag.

let doc = document.querySelector('article');
doc.removeChild(doc.lastElementChild);

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

let h2 = document.querySelector('h2');
h2.addEventListener("click",(e) => {e.target.style.backgroundColor = "red"} )

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

let h3 = document.querySelector('h3');
h3.addEventListener("click",(e) => {e.target.style.display = "none"} )

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
let makeBoldAll = () => {

    [...doc.children].forEach(e => e.style.fontWeight="bold")

}

let btn = document.createElement("button");
btn.innerHTML = "Click Me";
document.body.appendChild(btn);
btn.addEventListener("click", makeBoldAll)


// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
let sizeOrigin = 0

let randomSize =(e) => {
   
 let size = Math.floor(Math.random() * 101)
 sizeOrigin = e.target.style.fontSize;
 e.target.style.fontSize = size+"px";
}


let resizeOrigine =(e) => {

    console.log (sizeOrigin)
    e.target.style.fontSize = sizeOrigin;
   }


let h1 =  document.querySelector('h1')
console.log(h1);
h1.addEventListener("mouseover", randomSize)
h1.addEventListener("mouseleave", (e) => {  e.target.style.fontSize = "sisizeOriginze";})
// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)


// Exercise 2 : Work With Forms
// Instructions
// Copy the code below, into a structured HTML file:

// <form>
//   <label for="fname">First name:</label><br>
//   <input type="text" id="fname" name="fname"><br>
//   <label for="lname">Last name:</label><br>
//   <input type="text" id="lname" name="lname"><br><br>
//   <input type="submit" value="Submit" id="submit">
// </form> 
// <ul class="usersAnswer"></ul>


// Retrieve the form and console.log it.
let form =document.querySelector('form')
console.log(form)

// Retrieve the inputs by their id and console.log them.


console.log(document.querySelector('#fname'))
console.log(document.querySelector('#lname'))
console.log(document.querySelector('#submit'))


// Retrieve the inputs by their name attribute and console.log them.

console.log(form.elements['myfname'])
console.log(form.elements['lname'])
console.log(form.elements['submit'])


// When the user submits the form (ie. submit event listener)




// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
// The output should be :

// <ul class="usersAnswer">
//     <li>first name of the user</li>
//     <li>last name of the user</li>
// </ul>


// Exercise 3 : Transform The Sentence
// Instructions
// Add this sentence to your HTML file then follow the steps :

// <p><strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
// <strong>end</strong> you <strong>will</strong> be great Developers!
// <strong>Enjoy</strong> the <strong>JavaScript </strong> lessons</p>


// In the JS file:

// Create a global variable named allBoldItems.

// Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

// Create a function called highlight() that changes the color of all the bold text to blue.

// Create a function called return_normal() that changes the color of all the bold text back to black.

// Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example


// Exercice 4 : Volume Of A Sphere
// Instructions
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:
// <!doctype html> 
// <html lang="en"> 
//     <head> 
//         <meta charset="utf-8"> 
//         <title>Volume of a Sphere</title> 
//         <style>  
//             body {
//                 padding-top:30px;
//             } 

//             label,input {
//                 display:block;
//             }  
//         </style> 
//     </head> 
//     <body> 
//         <p>Input radius value and get the volume of a sphere.</p> 
//         <form  id="MyForm"> 
//             <label for="radius">Radius</label><input type="text" name="radius" id="radius" required> 
//             <label for="volume">Volume</label><input type="text" name="volume" id="volume"> 
//             <input type="submit" value="Calculate" id="submit">    
//         </form> 
//     </body> 
// </html> 


// Bonus Exercise 5 : Event Listeners
// Instructions
// Add as many events listeners as possible to one element on your webpage. Each listener should do a different thing, for instance- change position x, change position y, change color, change the font size… and more.
