a = 33
b = 200

number = int(input("enter number between 1 to 100"))
print(type(number))

if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
elif number % 3 == 0 :
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")

else:
    print("no good")

