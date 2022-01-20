// Exercise 1 : Change The Navbar
// Instructions
//  <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>

document.querySelector('#navBar').id = "socialNetworkNavigation";
let a = document.createElement('a');
a.appendChild(document.createTextNode('Logout'))
a.href = "#";
let li = document.createElement('li')
li.appendChild(a)
document.querySelector('ul').appendChild(li);


// In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.
// 
//We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (li).
// Finally, append this updated list node to the unordered list above, using the appendChild method.
//
// Bonus
// Use the firstElementChild and the lastElementChild properties to retrieve the first and last li 
//elements from their parent element (ul). Display the text of each link. 
//(Hint: use the textContent property).

//console.log(document.querySelector('ul').firstElementChild.textContent);
//console.log(document.querySelector('ul').lastElementChild.textContent);


// Exercise 2 : Users
// Instructions
// <html>
// <body>
//   <div id="container">Users:</div>
//   <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
//   </ul>
//   <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
//   </ul>
// </body>
// </html>


// In the HTML above change the name “Pete” to “Richard”.
console.log(document.querySelector('.list').lastElementChild.textContent);
document.querySelector('.list').lastElementChild.textContent = "richard";
// Change each first name of the two <ul>'s to your name.
document.querySelectorAll('.list').forEach(Element => {
    Element.firstElementChild.textContent = "stephane"
});


// At the end of each <ul> add a <li> that says “Hey students”.
let li2 = new Array(2)
li2[0] = document.createElement('li');
li2[1] = document.createElement('li');
//console.log(li2);
li2.map(item => {
    //item = document.createElement('li')
    item.appendChild(document.createTextNode("hey student"))
    console.log(item)
});
//console.log(document.querySelectorAll('.list'))

document.querySelectorAll('.list').forEach((item, index) => {
    // console.log(item)
    // console.log(index)
    console.log(li2[index])
    item.appendChild(li2[index]);
});
// document.querySelectorAll('.list').appendChild(li);
// Delete the name Sarah from the second <ul>.

// Bonus
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.


// Exercise 3 : Users And Style
// Instructions
// <html>
// <body>
//   <div>Users:</div>
//   <ul>
//     <li>John</li>
//     <li>Pete</li>
//   </ul>
// </body>
// </html>


// For the following exercise use the HTML presented above:

// Add a “light blue” background color and some padding to the <div>.
// Do not display the first name (John) in the list.
// Add a border to the second name (Pete).
// Change the font size of the whole body.
// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).