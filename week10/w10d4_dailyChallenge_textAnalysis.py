# Download the_stranger.txt
# Create a class called Text that takes a string as an argument and store the text in a attribute.

class Text:
    def __init__(self):
        with open('the_stranger.txt', 'r') as f:
            self.txt = f.read()
            #elf.list_words = self.var_words.splitlines()

    #def

# Implement the following methods:

# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message .



# a method that returns the most common word in the text.


# a method that returns a list of all the unique words in the text.


# a classmethod that returns a Text instance but with a text file: >>> Text.from_file('the_stranger.txt')

    @classmethod
    def return_text(cls):
        pass
#
# Create a class called TextModification that inherits from Text.
class TextModification(Text):
    def __init__(self):
        pass
# Implement the following methods:
# a method that returns the text without any punctuation.
    def del_ponctuation(self):
        self.txt_no_punct = self.txt.replace('\n', ' ').replace('  ', ' ').translate(str.maketrans('', '', ',.:;"?/'))
# a method that returns the text without any english stop-words (check out what this is !!).

# a method that returns the text without any special characters.
# Now, use the provided txt file and try using the class you created above.
# Note: Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)
#
with open('the_stranger.txt', 'r') as f:
    txt = f.read().replace('\n', ' ').replace('  ', ' ').translate(str.maketrans('', '', ',.:;"?/'))
    txt = f.read().replace('\n', ' ').replace('  ', ' ').translate(str.maketrans('', '', 'I it are is'))
print(txt)