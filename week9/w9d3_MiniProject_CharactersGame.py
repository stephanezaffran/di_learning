from math import *

# Description
# Create a class called Character with the following attributes and methods:
# name
# life – starts with a default value of 20
# attack – the base attack of a character (integer) will be a default of 10
# basic_attack() - accepts another character as a parameter and will <attack> the character and the characters <life> points should drop.

class Character:
    total_number_of_characters = 0       

    def __init__(self, name):
        self.__name = name
        self.__life = 20
        self.__attack = 10
        Character.total_number_of_characters += 1

    @property
    def name(self): 
        return self.__name

    @name.setter
    def name(self, value): 
        self.__name = value

    @property
    def life(self): 
        return self.__life

    @life.setter
    def life(self, value): 
        self.__life = value

    @property
    def attack(self): 
        return self.__attack

    @attack.setter
    def attack(self, value): 
        self.__attack = value

# Instructions
# Now create 3 different classes that inherit from Character:
# Every character type should say (ie. print) something when they are created, get creative :)

# Druid:
class Druid(Character):
    def __init__(self,name):
        super().__init__(name)
        print(f"new druid called: {self.name} was created, you now have {Character.total_number_of_characters} character in the game")
        
# meditate() - increase life by 10, decrease attack by 2
    def meditate(self):
        print(f"druid {self.name} meditate , old attack value {self.attack} old life value {self.life}  ", end=' ')
        self.life += 10
        self.attack -= 2
        print(f"new attack value {self.attack} , new life value {self.life} ")

# animal_help()- increase attack by 5
    def animal_help(self):
        print(f"druid {self.name} animal_help , old attack value {self.attack} ", end=' ')
        self.attack += 5
        print(f"new attack value {self.attack} ")
# fight() - accepts another character as a parameter and subtracts (0.75*life + 0.75*attack) from the other characters life.
# Example:
# druid.fight(other_char): other_char.life - (0.75*self.life + 0.75*self.attack)
    def fight(self, other_char: Character):
        print(f"druid {self.name}  fight to {other_char.name} , old life value {other_char.life} ", end=' ')
        other_char.life -= floor(0.75*(self.life+self.attack))
        # print("")
        # print(f"druid life{self.life} attack {self.attack} {floor(0.75*(self.life+self.attack))}")
        print(f"new {other_char.name} life value {other_char.life} ")
   

# Warrior:

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"new Warrior was created, you now have {Character.total_number_of_characters} character in the game")
   
# brawl() - accepts another character as a parameter, subtacts (2*attack) to the other characters life and adds (0.5*attack) to his own life.
    def brawl(self, other_char: Character):
        print(f"warrior {self.name} brawl to {other_char.name} , old life value {other_char.life}", end=' ')
        other_char.life -= 2
        self.attack += 0.5
        print(f"new {other_char.name} life value {other_char.life} ")



# train() - increase both your attack and life points by 2.
    def train(self):
        print(f"warrior {self.name} train , old  attack  value {self.attack} and old life value {self.life}")
        self.life += 2
        self.attack += 2
        print(f"warrior {self.name} train , new  attack  value {self.attack} and new life value {self.life}", end=' ')

# roar() - accepts another character as a parameter and subtracts their attack points by 3.
    def roar(self, other_char: Character):
        print(f"warrior {self.name} brawl to {other_char.name} , old attack value {other_char.attack}", end=' ')
        other_char.attack -= 3      
        print(f"new {other_char.name} attack value {other_char.attack} ")

# Mage:

class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"new Mage was created, you now have {Character.total_number_of_characters} character in the game")
        
# curse() – accepts another character as a parameter and subtracts their attack points by 2.
    def curse(self, other_char: Character):
        print(f"warrior {self.name} curse to {other_char.name} , old {other_char.name} attack value {other_char.attack}", end=' ')
        other_char.attack -= 2      
        print(f"new {other_char.name} attack value {other_char.attack} ")

# summon() - increases attack attribute by 3 points.
    def summon(self):
        print(f"mage {self.name} summon , old attack value {self.attack}", end="")
        self.attack += 3   
        print(f" new attack value {self.attack}")

# cast_spell() - accepts another character as a parameter and subtracts attack/life to the other characters life points (eg if your attack is 20 and life is 5 you will subtract 4 life points).
    def cast_spell(self, other_char: Character):

        print(f"warrior {self.name} cast_spell to {other_char.name} , old {other_char.name} attack value {other_char.attack}", end=' ')
        other_char.attack -= floor(self.attack/self.life)    
        print(f"new {other_char.name} attack value {other_char.attack} ")

# Once all your classes are created start testing them, create one of each character and use each of their methods.


fdruid = Druid("fdruid")
fwarrior = Warrior("fwarrior")
fmage = Mage("fmage")

fdruid.meditate()
fdruid.animal_help()
fdruid.fight(fwarrior)

fwarrior.train()
fwarrior.roar(fdruid)
fwarrior.brawl(fmage)

fmage.summon()
fmage.curse(fwarrior)
fmage.cast_spell(fdruid)
