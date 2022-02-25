# Mini Project : Vaccines
# Vaccines Management System
# Your goal is to create a program to help a city with the vaccination of its citizens.

# Part 1
# You will have to create two classes:

# Human
# Queue
# Here is a description of them:

# 1) Human
# Represents a citizen of the city, it has the following attributes: id_number (str), name (str), 
# age (int), prioritary (bool)  and blood_type (str).  Its blood type can be “A”, “B”, “AB” or “O”.

# It got no methods.

class Human:
    def __init__(self, id_number:str, name: str, age: int, prioritary: bool, blood_type: str = "A"):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.prioritary = prioritary
        if blood_type in ["A","B","AB","O"]:
            self.blood_type = blood_type

    def __str__(self):
	    return f" {'-'* 20}\nid_number: {self.id_number} \nname : {self.name} \nage:  {self.age} \nprioritary : {self.prioritary} \nblood_type:  {self.blood_type}"
# 2) Queue
# Represents a queue of humans waiting for their vaccine. It has two attributes, humans, the list containing the humans 
# that are waiting, it is initialized empty.
# This class is useful to manage who will get vaccinated in priority. It has the following methods:
class Node:
   def __init__(self, human=None):
      self.human = human
      self.next_node = None
      self.preview_node = None

class Head_list:
   def __init__(self):
      self.first_elem = None


class Queue:
    def __init__(self):
        self.humans_first_node = Head_list()
        self.humans_waiting_first_node =  Head_list()
        self.last_humans_node = self.humans_first_node
        self.human_waiting_last_node = self.humans_waiting_first_node

# add_person(self, person) Add a human to the queue, if he is older than 60 years old or a prioritary person, put him at the beginning of the list (at index 0) before every other.
    def add_person(self, person: Human):
        #if empty list , start with head_list
        if  self.humans_first_node == self.last_humans_node:
            self.humans_first_node.first_elem = Node(person)
            self.humans_first_node.first_elem.preview_node = self.humans_first_node
            self.last_humans_node = self.humans_first_node.first_elem
        #if there are nodes, add at the end for youngs or at the begging if old person
        else:
            #add at the end if not priority person
            if person.age < 60 and person.prioritary == False:
                self.last_humans_node.next_node = Node(person)
                self.last_humans_node.next_node.preview_node = self.last_humans_node
                self.last_humans_node = self.last_humans_node.next_node
            
            else:
            #add at the begining for priority person
                temp = Node(person)
                temp.next_node = self.humans_first_node.first_elem
                temp.next_node.preview_node = temp
                temp.preview_node = self.humans_first_node
                self.humans_first_node.first_elem = temp

# find_in_queue(self, person) Returns the index of a human in the queue.
    def find_in_queue(self, person: Human):
       temp = self.humans_first_node.first_elem
       while temp != self.last_humans_node:
            #print(f"id_number: {temp.human.id_number} name: {temp.human.name}")
            if temp.human.id_number == person.id_number:                
                #remove the person from the list
               # temp.next_node.preview_node = temp.preview_node
               #  if temp.preview_node != self.humans_first_node:
               #      temp.preview_node.next_node = temp.next_node
               #  else:
               #      self.humans_first_node = temp.next_node
               #  temp.next_node = None
               #  temp.preview_node = None
                return temp
            else:
                temp = temp.next_node
       if temp.human.id_number == person.id_number:
           # temp.preview_node.next_node = None
           return temp
       else:
           return None
    
# swap(self, person1, person2) Swaps person1 with person2.
    def swap(self, person1, person2):
        temp1 = self.find_in_queue(person1)
        temp2 = self.find_in_queue(person2)
        t_person = temp2.human
        temp2.human = temp1.human
        temp1.human = t_person

# get_next(self) return the next human in the queue, meaning the object at index 0 in the list.
    def get_next(self):
        #check if the queue is not empty
        if  self.humans_first_node != self.last_humans_node:
            temp = self.humans_first_node.first_elem.human
            self.humans_first_node.first_elem = temp.next_node            
            temp.next_node = None
            temp.preview_node = None
            return temp.human

            #check if del of node don't remove the instance of human inside
            #next_person = temp.human
            #del temp
            #return next_person


# get_next_blood_type(self, blood_type) Return the first human with this specific blood type.
    def get_next_blood_type(self, blood_type):
        index = 1
        temp = self.humans_first_node.first_elem
        while temp != self.last_humans_node:
            if temp.human.blood_type == blood_type:
                #remove the person from the list
                temp.next_node.preview_node = temp.preview_node
                temp.preview_node.next_node= temp.next_node
                temp.next_node = None
                temp.preview_node = None
                return temp.human
            else:
                temp = temp.next_node
        return None

# sort_by_age(self) Sort the queue so that the older ones are before the younger ones and all the prioritary persons are before the others.
    def sort_by_age(self):
        cursor1 = self.humans_first_node.first_elem
        while cursor1 != self.last_humans_node:
            cursor2 = cursor1.next_node
            while cursor2 != self.last_humans_node:
                if cursor1.human.age < cursor2.human.age:
                    self.swap(cursor1.human, cursor2.human)
                    cursor2 = cursor2.next_node
                else:
                    cursor2 = cursor2.next_node
            if cursor1.human.age < cursor2.human.age:
                self.swap(cursor1.human, cursor2.human)
            cursor1 = cursor1.next_node
        print("toto")
# Every human returned by get_next and get_next_blood_type is removed from the list,
#  those functions return None if there is no one in the list.

    def __str__(self):
        if self.humans_first_node == self.last_humans_node:
            return
        else:
            temp = self.humans_first_node.first_elem
            print(f"{'-'* 50}")
            while temp != self.last_humans_node:
                print(temp.human)
                temp = temp.next_node
            print(temp.human)
my_queue = Queue()
p1= Human(1, "aaa", 1, False, "A")
p2= Human(2,"bbb",2,True,"B")
p3= Human(3,"ccc",3,False,"A")
p4= Human(4,"ddd",70,False,"AB")
p5= Human(5,"eee",57,False,"AB")
my_queue.add_person(p1)
my_queue.add_person(p2)
my_queue.add_person(p3)
my_queue.add_person(p4)
my_queue.add_person(p5)

p4bis = my_queue.find_in_queue(p5)
print(p4bis.human)
my_queue.swap(p4, p1)
#print(my_queue)
my_queue.sort_by_age()
print(my_queue)

# Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.

# Part 2
# Create an attribute family for the Human class. Initialized as empty, family is a list of all the humans that are living in the same house with this human. Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.

# Add the rearange_queue(self) method to the Queue class, so that there is no two members of the same family one after the other.


