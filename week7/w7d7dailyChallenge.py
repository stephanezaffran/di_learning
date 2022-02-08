# Hint: Look at the remote learning “Matrix” videos
#
# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, select only the alpha characters and connect them,
# then he replaces every group of symbols between two alpha characters by a space.
#
# Using his technique, try to decode this matrix:
#     7i3
#     Tsi
#     h%x
#     i #
#     sM
#     $a
#     #t%
#     ^r!
# alpha = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
decoded_message = ""

#error message PEP 8: E501 line too long (129 > 120 characters) ????
alpha = {"a",  "f", "g", "h", "i", "T", "M", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
code = ["7i3", "Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "^r!"]
number_of_symbols = 0
for x in range(3):
    for index, item in enumerate(code):
        if code[index][x] in alpha:
            number_of_symbols = 0
            decoded_message += code[index][x]
        else:
            print(f"value of symbole : {code[index][x]}")
            number_of_symbols += 1
            if number_of_symbols == 2:
                decoded_message += " "

print(decoded_message)