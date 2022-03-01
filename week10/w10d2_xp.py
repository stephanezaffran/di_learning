#
# Exercise 1
# Choose any function you wrote in the functions chapter and store it in a separate file then use import with the following syntaxes:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn

# generate random integer values
from string import ascii_uppercase,ascii_lowercase
from random import randint, random, choice
import module1
import w9d1_create_modules.operator
from w9d1_create_modules.operator import addOperator
from w9d1_create_modules.operator import divideOperator as my_divid



#
#
# Exercise 2
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.
#
def compare_number_to_rand(number):
	return "congratulation" if number == randint(1, 100) else None
#
# Exercise 3
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

def string_generator():
	chars = ascii_uppercase + ascii_lowercase
	return ''.join(choice(chars) for _ in range(5))

for x in range(6):
	print(string_generator())

