# Part I - Game.Py
# game.py – this file/module should contain a class called Game. It should have 4 methods:
# get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.
#
# get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).
#
# get_game_result(self, user_item, computer_item) – Determine the result of the game.
# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
#
# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
from random import randint, choices

class Game:
	def __init__(self):
		self.items = ["rock", "paper", "scissors"]
		self.rules = {
			"rock": "scissors",
			"paper": "rock",
			"scissors": "paper"
		}

	def get_user_item(self):
		while 1:
			user_item = input("Enter your choice rock, paper or scissors ")
			if user_item.lower() in self.items:
				return user_item.lower()



	def get_computer_item(self):
		rand = randint(0, 2)
		return self.items[rand]
		#random.choice(self.item)

	def get_game_result(self, user_item, computer_item):
		if user_item == computer_item:
			return "same choice"
		elif self.rules[user_item] == computer_item:
			return "you win"
		else:
			return "you lost"

	def play(self):
		#user_item = computer_choice =""
		#while user_item == computer_choice:
		user_item = self.get_user_item()
		computer_choice = self.get_computer_item()
		result = self.get_game_result(user_item, computer_choice)
		print(f"You selected {user_item}, the computer selected {computer_choice}, {result}")


var = true
while var:
	Game().play()
# Get the user’s item (rock/paper/scissors) and remember it
#
# Get a random item for the computer (rock/paper/scissors) and remember it
#
# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”
#
# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
#
#
