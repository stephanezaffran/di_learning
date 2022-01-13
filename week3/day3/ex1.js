let people = ["Greg", "Mary", "Devon", "James"]
console.log(people);
//people.splice(0,1);
people.shift();
console.log(people);
people.splice(2,1,"Jason")
console.log(people);
people.push("stephane")
console.log(people);
console.log(people.indexOf("Mary"));
let peopleCopy = people.slice(1,3);
console.log(peopleCopy)
console.log("foo index " + people.indexOf("Foo")); //not exist

for(let person of people){
    console.log(person);
}

for(let person of people){
    if(person == "Jason"){
        console.log( "yeah " + person + " is here");
        break;
    }
}



console.log("...............Exercise 2..................");

let colors = ["blue", "green", "white", "black"];
let suffix = "";
for (let index in colors){
    if(index == 0){suffix = "st"};
    if(index == 1){suffix = "nd"}
    if(index == 2){suffix = "rd"}
    if(index == 3){suffix = "th"}

    console.log("my " + (parseInt(index)+1) + suffix + " choice is colour " +  colors[index]);

}


console.log("...............Exercise 3..................");



// let result = prompt("enter a number")
// console.log(typeof(result));

// result = 0 ;
// while(result < 10){
//    result = prompt("enter a number")
// }



console.log("..............Exercise 4...................");


let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}

console.log("the number of floors in the building is " + building.numberOfFloors);
console.log(  building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor + " apartments are on the floors 1 and 3 ");
console.log(`the name of the second tenant  is  ${Object.keys(building.numberOfRoomsAndRent)[1]}  and the number of rooms in his apartment is ${Object.values(building.numberOfRoomsAndRent)[1][0]}` );

if(building.numberOfRoomsAndRent.sarah[1]+building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1] ){
    building.numberOfRoomsAndRent.dan[1] = 1200;
}
console.log(building.numberOfRoomsAndRent.dan[1])

console.log("...............Exercise 5..................");

let family = { 
    father : "dan",
    sister : "lea",
    brother : "david" 
};

    for(let familyMember in family){
        console.log(`${familyMember}: ${family[familyMember]}`)
      //  console.log(object.values(family[familyMember]))
    }


// for (const property in object) {
//     console.log(`${property}: ${object[property]}`);
//   }
    
for (let [key, value] of Object.entries(family)) {
    console.log(key, value);
  }



  console.log("...............Exercise 6..................");


  let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }

  let sentenceComplete ="";
  for(let detail in details){
    sentenceComplete += detail + " " + details[detail] + " " ;
  }
  console.log(sentenceComplete)

  console.log("...............Exercise 7..................");

  let secretName = "";
  let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
names = names.sort();
for(let name of names)(
    secretName+=name[0]
)
console.log(secretName);


console.log("...................tests ..............");



 names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
let strNames="";
for(let name in names){
    console.log(name);
    strNames += names.slice(parseInt(name),parseInt(name)+1) + " , ";
   // console.log(names.slice(parseInt(name),parseInt(name)+1));
}
console.log(strNames);

let person ={ name: 'stephane' , tel : '123456'};
for(let pers in person){
    console.log(person[pers])
}