# Part II - Rock-Paper-Scissors.Py
# rock-paper-scissors.py : create 3 functions
# get_user_menu_choice() - this should display a simple menu, get the user’s choice (with data validation), and return the choice. No looping should occur here.
# The possibles choices are : Play a new game or Show scores or Quit
#
def get_user_menu_choice():
	while 1:
		print(" 1 - Play a new game "
		      " 2 - Show scores or Quit"
		      " 3 - quit")

		Game().play()
# print_results(results) – this should print the results of the games played. It should have a single parameter named results; which will be a dictionary of the results of the games played. It should display these results in a user-friendly way, and thank the user for playing.
#
#
# Note: results should be in this form: {win: 2,loss: 4,draw: 3}. Bear in mind that this dictionary will need to be created and populated in some other part of our code, and passed in to the print_results function at the right time.
#
# main() - the main function. It should take care of 3 things:

def main():


# Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’, whatever you decide. (Make use of the get_user_menu_choice function)
#
# When the user chooses to play a game:
# Create a new Game object (see below), and call its play() function, receiving the result of the game that is returned.
# Remember the results of every game that is played.
#
# When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.
#
