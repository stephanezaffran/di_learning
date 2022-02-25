# Exercise 1

# Create a class Human, it has the following attributes:
# name (str)
# age (int)
# living_place (Building - Default is None)
# Add the move(self, building) method to the Human class, it sets the living place of this human to the building and add this human to the building inhabitants.

class Human:
    def __init__(self, name, age, living_place = None ):
        self.name = name
        self.age = age
        self.living_place = living_place

    
    def move(self, building):
        self.living_place = building.address
        building.inhabitants.append(self)



# Create  class Building, it has the following attributes:
# address (str)
# inhabitants (List of Human objs - Default is empty)

class Building:
    def __init__(self, address, inhabitants = [] ):
        self.address = address
        self.inhabitants = inhabitants


tom = Human("tom", 18)
eli = Human("eli", 22)
b1 = Building("1 israel street")
b2 = Building("1 paris street")
tom.move(b1)
eli.move(b1)

print(len(b1.inhabitants))
print(b1.inhabitants[0].name)
print(b1.inhabitants[1].name)
print(eli.living_place)
tom.move(b1)
print(eli.living_place)

# Create a class City, it has the following attributes:
# name (str)
# buildings (List of Building objs - Default is empty)
# Add the construct(self, address) method to the City class, it adds a building at the referenced address.
# Add the info(self, address) method to the City class, it displays the number of buildings and the mean age of the citizens.
class City:
    def __init__(self, name, buildings = [] ):
        self.name = name
        self.buildings = buildings
  
    def construct(self, address):
        building = Building(address) 
        self.buildings.append(building)

    def info(self, address):
        pass


paris = City("paris")
paris.construct("champs elyse street")
paris.construct("paix street")
print(len(paris.buildings))
print(paris.buildings[1].address)