# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Suppose the following input is supplied to the program:
# without,hello,bag,world

my_txt = "without,hello,bag,world"


def sort_str(txt):
	splited_text = txt.split(",")
	sort_list = sorted(splited_text, key=str.lower)
	sorted_str = ",".join(sort_list)
	return sorted_str


print(sort_str(my_txt))

# Then, the output should be:
# bag,hello,without,world
