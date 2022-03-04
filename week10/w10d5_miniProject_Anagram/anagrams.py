# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program,
# and will rely on AnagramChecker for the anagram-related logic.
#
# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
#

import anagram_checker


class ui:
	def __init__(self):

		self.checker = anagram_checker.AnagramChecker()
		self.loop = True

		while (self.loop):

			self.userInput = input("please enter a single word with only alphabetic characters  ").strip()
			if ' ' in self.userInput:
				print("not regular word, more than one word, try again")
			elif not self.userInput.isalpha():
				print("not regular word,  only alphabetic characters are allowed, try again")
			else:

				print(self.checker.get_anagrams(self.userInput))

			if input("for quit insert q ") == 'q':
				self.loop = False

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input. --> strip
#
# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:
#
#
# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.


loop1 = ui()