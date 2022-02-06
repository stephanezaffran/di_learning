# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dic ={}
for item in zip(keys,values):
    my_dic[item[0]] = item[1]
print(my_dic)

#
# Exercise 2 : Cinemax #2
# Instructionsday
# “Continuation of Exercise Cinemax from Week4Day2 XP”
#
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Given the following object:
#
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
#
# How much does each family member have to pay ?

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_sum = 0

for x, y in family.items():
    if y < 3:
        print(f" for {x} the price is free.")
    if y >= 3 and y <= 12:
        print(f" for {x} the price is $10.")
        total_sum += 10
    if y > 12:
        print(f" for {x} the price is $15.")
        total_sum += 15




#
# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
#
print(f" total to pay for the family {total_sum}.")



# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green
#
#
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}

# 3. Change the number of stores to 2.
brand['number_stores'] = 2

# 4. Print a sentence that explains who Zaras clients are.



# 5. Add a key called country_creation with a value of Spain.

brand['country_creation'] = "Spain"

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

brand['international_competitors'].append("Desigual")

# 7. Delete the information about the date of creation.

del brand['creation_date']

# 8. Print the last international competitor.

# leng = len(brand['international_competitors'])
print(brand['international_competitors'][-1])

# 9. Print the major clothes colors in the US.

print(brand['major_color']["US"])

# 10. Print the amount of key value pairs (ie. length of the dictionary).

print(len(brand))

# 11. Print the keys of the dictionary.

for x in brand.items():
    print(x[0])

# 12. Create another dictionary called more_on_zara with the following details:
#
# creation_date: 1975
# number_stores: 10 000
#
more_on_zara = {
"creation_date": 1975,
"number_stores": 10000
}

#
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

for x, y in more_on_zara.items():
    brand[x] = y

# 14. Print the value of the key number_stores. What just happened ?


    print(brand["number_stores"])

# we update the number of stores




#
#
# Exercise 4 : Disney Characters
# Instructions
# Use this list :
#
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# Analyse these results :
#
# #1/
#
users = [ "Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}


disney_users_A ={}

for index, item in enumerate(users):
    disney_users_A[item] = index
print(disney_users_A)


#
# #2/
#
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
disney_users_B = {}
for index, item in enumerate(users):
    disney_users_B[index] = item
print(disney_users_B)


# #3/
#

disney_users_c ={}
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
#
#
# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.
