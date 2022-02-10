# Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
#
#
# Hint
# To do this project, you basically need to create four functions:
#
# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely different appoach if you want.
#
#

screen = [
	["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
	["*", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "*"],
	["*", "-", "-", "-", "|", "-", "-", "-", "|", "-", "-", "-", "*"],
	["*", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "*"],
	["*", "-", "-", "-", "|", "-", "-", "-", "|", "-", "-", "-", "*"],
	["*", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "*"],
	["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
]


def get_column_place(column):
	column = int(column)
	if column == 1:
		return 2
	elif column == 2:
		return 6
	elif column == 3:
		return 10
	else:
		return -1


def get_row_place(row):
	row = int(row)
	if row == 1:
		return 1
	elif row == 2:
		return 3
	elif row == 3:
		return 5
	else:
		return -1


def display_board():  # –  To display the Tic Tac Toe board (GUI).

	for i in screen:
		for j in i:
			print(j, end='')
		print('')


def player_input(player):  # – To get the position from the player.
	while 1:
		print(f"player {player} turn .....")
		column = input("enter column ")
		row = input("enter row ")
		# check if the place is free
		if int(get_row_place(row)) != -1 and int(get_column_place(column)) != -1:
			if screen[int(get_row_place(row))][int(get_column_place(column))] == " ":
				return get_column_place(column), get_row_place(row)
			else:
				print("this place still occuped ")
		else:
			print("bad column or bad row, try again ")


def player_choice(player, row, column):
	screen[int(row)][int(column)] = player
	display_board()


def check_win():  # – To check whether there is a winner or not.
	# check vertical
	if screen[1][2] == "x" and screen[1][6] == "x" and screen[1][10] == "x":
		return "xwin"
	elif screen[3][2] == "x" and screen[3][6] == "x" and screen[3][10] == "x":
		return "xwin"
	elif screen[5][2] == "x" and screen[5][6] == "x" and screen[5][10] == "x":
		return "xwin"
	# check vertical
	elif screen[1][2] == "x" and screen[3][2] == "x" and screen[5][2] == "x":
		return "xwin"
	elif screen[1][6] == "x" and screen[3][6] == "x" and screen[5][6] == "x":
		return "xwin"
	elif screen[1][10] == "x" and screen[3][10] == "x" and screen[5][10] == "x":
		return "xwin"
	# check diagonal
	elif screen[1][2] == "x" and screen[3][6] == "x" and screen[3][10] == "x":
		return "xwin"
	elif screen[1][10] == "x" and screen[3][6] == "x" and screen[5][2] == "x":
		return "xwin"

	# check vertical
	elif screen[1][2] == "o" and screen[1][6] == "o" and screen[1][10] == "o":
		return "owin"
	elif screen[3][2] == "o" and screen[3][6] == "o" and screen[3][10] == "o":
		return "owin"
	elif screen[5][2] == "o" and screen[5][6] == "o" and screen[5][10] == "o":
		return "owin"
	# check vertical
	elif screen[1][2] == "o" and screen[3][2] == "o" and screen[5][2] == "o":
		return "owin"
	elif screen[1][6] == "o" and screen[3][6] == "o" and screen[5][6] == "o":
		return "owin"
	elif screen[1][10] == "o" and screen[3][10] == "o" and screen[5][10] == "o":
		return "owin"
	# check diagonal
	elif screen[1][2] == "o" and screen[3][6] == "o" and screen[3][10] == "o":
		return "owin"
	elif screen[1][10] == "o" and screen[3][6] == "o" and screen[5][2] == "o":
		return "owin"

	# check if not full grid
	if screen[1][2] != " " and screen[1][6] != " " and screen[1][10] != " " and screen[3][2] != " " and screen[3][6] != " " and screen[3][10] != " " and screen[5][2] != " " and screen[5][6] != " " and screen[5][10] != " ":
		return "finish"

	return "continue"


def play():  # – The main function, which calls all the functions created above.
	mod = 1
	players = ['x', 'o']
	print("welcome to tic tac toe")
	display_board()
	status = "continue"
	while status == "continue":
		player = players[mod % 2]
		column, row = player_input(player)
		player_choice(player, row, column)
		status = check_win()
		# print(f"column: {column} row: {row} ")
		mod += 1
	if status == "xwin":
		print("X win ")
	elif status == "owin":
		print("O win ")
	elif status == "finish":
		print("game finish , no winner")

play()
# Tips : Consider The Following:
# What functionality will need to accur every turn to make this program work?
# After contemplating the question above, think about splitting your code into smaller pieces (functions).
# Remember to follow the single responsibility principle! each function should do one thing and do it well!
