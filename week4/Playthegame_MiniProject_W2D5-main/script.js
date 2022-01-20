let playTheGame = () => {
    let number = ""
    let computerNumber = Math.floor(Math.random() * 10);
    let count = 0
    let mytest = 0
    let play = confirm("do you want to play the game ?")
    switch (play) {
        case false:
            alert("No problem, Goodbye")

            break;
        case true:
            while (true) {
                if (count >= 3) {
                    alert(`out of chances number was ${computerNumber} `)
                    break
                }
                number = parseInt(prompt("please  enter a number between 0 and 10 "))
                if (Number.isNaN(number)) {
                    alert("Sorry Not a number, Goodbye")
                    break;
                } else {

                    if (number < 0 || number > 10) {
                        alert("Sorry it’s not a good number, Goodbye")
                        break;
                    } else {
                        if (test(computerNumber, number) == "equal") {
                            alert("winner");
                            break
                        } else if (test(computerNumber, number) == "sup") {
                            alert("Your number is bigger then the computer's,guess again")
                            count++;
                        } else if (test(computerNumber, number) == "inf") {
                            alert("Your number is smaller then the computer's,guess again")
                            count++
                        }
                    }
                }
            }
            break;
        default:
            break;
    }
}


let test = (computerNumber, userNumber) => {
    if (userNumber == computerNumber) { return "equal" } else if (userNumber > computerNumber) { return "sup" } else if (userNumber < computerNumber) { return "inf" }
}

// Outside of the playTheGame() function, create a new function named test(userNumber,computerNumber)
// that takes 2 parameters : userNumber and computerNumber

// The point of this function is to check if the userNumber is the same as the computerNumber:
// If userNumber is equal to computerNumber, alert “WINNER” and stop the game.

// If userNumber is bigger than computerNumber, alert “Your number is bigger then the computer’s,
// guess again” (Hint: use the built-in prompt() function to ask the user for a new number).

// If userNumber is lower than computerNumber, alert “Your number is smaller then the computer’s, 
//guess again” (Hint: use the built-in prompt() function to ask the user for a new number).

// If the user guessed more than 3 times, alert “out of chances” and exit the function.