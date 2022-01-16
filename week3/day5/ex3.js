let year1 = prompt("please enter the first born year ?")
let year2 = prompt("please enter the second born year ?")

if (year1 > year2) {
    let yearTheSameAge = (year1 - year2) + year1
} else {
    let yearTheSameAge = (year2 - year1) + year2
}
alert(yearTheSameAge)