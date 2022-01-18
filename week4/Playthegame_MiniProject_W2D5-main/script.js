function playTheGame() {
    let play = confirm("do you want to play th game ?")
    switch (play) {
        case false:
            alert("No problem, Goodbye")

            break;
        case true:
            let number = prompt("please  enter a number between 0 and 10 ")
            if (typeof number != 'number') {
                alert("Sorry Not a number, Goodbye")

            } else {
                if (number < 0 && number > 10) {
                    alert("Sorry it’s not a good number, Goodbye")
                } else {
                    let computerNumber = Math.random();


                }

            }
            break;

        default:
            break;
    }
}

let test = (userNumber, computerNumber) => {

}

// Outside of the playTheGame() function, create a new function named test(userNumber,computerNumber)
// that takes 2 parameters : userNumber and computerNumber

// The point of this function is to check if the userNumber is the same as the computerNumber:
// If userNumber is equal to computerNumber, alert “WINNER” and stop the game.

// If userNumber is bigger than computerNumber, alert “Your number is bigger then the computer’s, guess again” (Hint: use the built-in prompt() function to ask the user for a new number).

// If userNumber is lower than computerNumber, alert “Your number is smaller then the computer’s, guess again” (Hint: use the built-in prompt() function to ask the user for a new number).

// If the user guessed more than 3 times, alert “out of chances” and exit the function.