#
# Exercise 1: Cats
# Instructions
# Using this class
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
#

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


my_cat = []
my_cat.append(Cat(name="cat1", age=1))
my_cat.append(Cat(name="cat2", age=2))
my_cat.append(Cat(name="cat3", age=3))

choosen_cat = max(my_cat, key=lambda x: x.age)

print(f"The oldest cat is {choosen_cat.name}, and is {choosen_cat.age} years old.")
#
# Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jumping = int(self.height.replace("cm", ""))*2
        print(f"{self.name} jumps {jumping} cm high!")


# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.

davids_dog = Dog(name="Rex", height="50cm")
davids_dog.jump()

# Print the details of his dog (ie. name and height) and call the methods bark and jump.
print(f"name of the dog : {davids_dog.name} and height : {davids_dog.height} !")


# Create an object called sarahs_dog. Her dog’s name is “Teacup”
sarahs_dog = Dog(name="Teacup", height="20cm")


# Print the details of her dog (ie. name and height) and call the methods bark and jump.
print(f"name of the dog : {sarahs_dog.name} and height : {sarahs_dog.height} !")


# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
#

print(f"biggest dog is :  { sarahs_dog.name if int(sarahs_dog.height.replace('cm', '')) > int(davids_dog.height.replace('cm', '')) else davids_dog.name }")

#
# Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        # print(list(map(lambda x: x, self.lyrics)))
        print('\n'.join(map(str, self.lyrics)))


# Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

# Then, call the sing_me_a_song method. The output should be:
stairway.sing_me_a_song()

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven
#
#
# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)


# Create a method called get_animals that prints all the animals of the zoo.
    def get_animals(self):
        print('\n'.join(map(str, self.animals)))

# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
    def sell_animal(self, animal_sold):
        index = self.animals.index(animal_sold)
        if index != -1:
            del self.animals[index]


# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
    def sort_animals(self):

        dic_index = 1
        my_dict = {}
        self.animals.sort()

        temp = []

        for index, elem in enumerate(self.animals):
            temp.append(elem)
            print(f"elem {elem} index {index} ")
            if index < len(self.animals)-1:
                if self.animals[index][0] != self.animals[index+1][0]:
                    my_dict[dic_index] = temp
                    dic_index += 1
                    temp = []
            elif index == len(self.animals)-1:
                my_dict[dic_index] = temp

        print(my_dict)

 # util_func = lambda x: x[0]
 # temp = sorted(test_list, key=util_func)
 # res = [list(ele) for i, ele in groupby(temp, util_func)]

# Example
#
# {
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
#
#
# Create a method called get_groups that prints the animal/animals inside each group.
#
# Create an object called ramat_gan_safari and call all the methods.

ramat_gan_safari = Zoo("ramat gan safari")
ramat_gan_safari.add_animal("g")
ramat_gan_safari.add_animal("c")
ramat_gan_safari.add_animal("aa")
ramat_gan_safari.add_animal("ab")
ramat_gan_safari.add_animal("ba")
ramat_gan_safari.add_animal("bb")
ramat_gan_safari.add_animal("ta")
ramat_gan_safari.add_animal("d")

ramat_gan_safari.sort_animals()

# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)
