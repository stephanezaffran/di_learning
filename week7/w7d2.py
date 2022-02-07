

import random

# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.
#
def display_message():
	print("the python course is very interesting ")


display_message()


#
# Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, make sure to include a book title as an argument when calling the function.
#
def favorite_book(title):
	print(f"One of my favorite books is {title}")


favorite_book("Alice in Wonderland")
#

# Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the country parameter a default value.
# Call your function.
#


def describe_city(name):

	print(f"One of my favorite books is {title}")


favorite_book("Alice in Wonderland")

#
# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
#

def check_rand(num):
	if num > 0 and num <= 100:
		rand = random.randint(1, 100)
		if num == rand:
			print("success")
		else:
			print(f"unsuccess {num} is different to {rand}")


check_rand(25)

#
# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function make_shirt() using positional arguments to make a shirt.
def make_shirt(size, text):
	print(f'we will print: "{text}" on the tshirt size: {size}')


make_shirt(size="L", text="beautifull shirt")


# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
# Bonus: Call the function make_shirt() using keyword arguments.
#
def make_shirt(size="L", text="I love python"):
	print(f'we will print: "{text}" on the tshirt size: {size}')

make_shirt()
make_shirt(size="M")
make_shirt(size="L")
make_shirt(size="S", text="beautifull shirt")

#
# Exercise 6 : Magicians …
# Instructions
# Make a list of magician’s names.
magicians = ["abracadabra", "nostradamus", "merlin", "oz"]
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
def show_magicians():
	for magician in magicians:
		print(magician)

#show_magicians(magicians)
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.

def make_great():
	for index, magician in enumerate(magicians):
		magician = magician + " the great"
		magicians[index] = magician
		print(magician)


# Call the function make_great().
make_great()
# Call the function show_magicians() to see that the list has actually been modified.
show_magicians()
