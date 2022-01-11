//exercise 1
console.log("exercise 1")

let food ="salmon";
let meal ="afternoon";
console.log("I eat " + food + " at every " + meal );

//exercise 2

console.log("exercise 2")

let watchedSeries = ["black mirror", "money heist", "the big bang theory"];

let watchedSeriesLength = watchedSeries.length;
console.log(watchedSeriesLength)

let myWatchedSeries = watchedSeries[0]+" , "+ watchedSeries[1]+" , "+watchedSeries[2];
console.log("I watched 3 series : "+ myWatchedSeries);

watchedSeries[2] = "friend";
myWatchedSeries = watchedSeries[0]+" , "+ watchedSeries[1]+" , "+watchedSeries[2];
console.log("I watched 3 series : "+ myWatchedSeries);

watchedSeries.push("dexter");
watchedSeries.splice(0,0,"doctor house");
myWatchedSeries = watchedSeries[0]+" , "+ watchedSeries[1]+" , "+watchedSeries[2]+" , "+watchedSeries[3]+" , "+watchedSeries[4];
console.log("I watched series : "+ myWatchedSeries);

watchedSeries.splice(1,1);
myWatchedSeries = watchedSeries[0]+" , "+ watchedSeries[1]+" , "+watchedSeries[2]+" , "+watchedSeries[3];
console.log("I watched series : "+ myWatchedSeries);

console.log(watchedSeries[1][2]);

//exercise 3
console.log("exercise 3")
let celcius = 30;
let fahrenheit = celcius/5;
console.log(celcius + " °C is " +fahrenheit + " °F");

//exercise xp 1
console.log("exercise xp 1")
let me = ["my","favorite","color","is","blue"];
let meString = me[0]+" "+me[1]+" "+me[2]+" "+me[3]+" "+me[4];
console.log(meString);

//exercise xp 2
console.log("exercise xp 2")
let str1 = "mix" ;
let str2 = "pod";
let strSwapped = str1.slice(0,2)+str2.slice(0,2);
console.log(strSwapped);