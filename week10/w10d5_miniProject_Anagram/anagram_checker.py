# Instructions
# First Download this text file : right click –> Save As
#
# Create a new file called anagram_checker.py which contains a class called AnagramChecker.
#

class AnagramChecker:

# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.

	def __init__(self):
		with open('sowpods.txt', 'r') as f:
			self.var_words = f.read()
			self.list_words = self.var_words.splitlines()

# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.

	def is_valid_word(self, word):
		return str.upper(word) in self.list_words

# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’,
# the function should return a list containing [“mate”, “tame”, “team”].)

	def get_anagrams(self, word):

		# filter the liste with is_valid_word to keep only valid words
		return(list(filter(lambda x: self.is_anagram(x, str.upper(word)), self.list_words)))


# Hint: you might want to create a separate method called is_anagram(word1, word2),
# that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.
#

	def is_anagram(self, word1, word2):
		# Strings are sorted and check whether both are matching or not
		return sorted(word1) == sorted(word2)


# Note: None of the methods in the class should print anything.
#

# def myfunc(a):
#   return a[0] + a[1]
#
#
# x = map(myfunc, {'apple': '1', 'banana' : '2', 'cherry' : '3'}.items() )
# print(x)
#
# file = AnagramChecker()
# print(list(file.get_anagrams("bara")))