let language = prompt("what's your language ?");
language = language.toLowerCase()
switch (language) {
    case "hebrew":
        alert("shalom")
        break;
    case "french":
        alert("salut")
        break;
    case "english":
        alert("hello")
        break;
    default:
        alert("01110011 01101111 01110010 01110010 01111001")
        break;
}

//.................ex2................
let grade = prompt("what's your grade ?");
grade = parseInt(grade);
if (grade > 90) {
    console.log("A")
} else if (80 < grade <= 90) {
    console.log("B")
} else if (70 <= grade <= 80) {
    console.log("C")
} else {
    console.log("D")
}



//.................ex3................
let verb = prompt("please enter a verb ?")
verb = verb.toLowerCase();
if (verb.lenght < 3) {
    break
} else {
    let index = verb.lenght;
    if (verb[index - 3] == 'i' && verb[index - 2] == 'n' && verb[index - 1] == 'g') {
        verb = verb + "ly";
    } else {
        verb = verb + "ing";
    }
}