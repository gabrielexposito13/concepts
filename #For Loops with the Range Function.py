#For Loops with the Range Function

#This will print 1 to 10: 
for number in range(1,11):
    print(number)

#This will print in steps of 3:
for number in range(1,11, 3):
    print(number)

# Gaus Sum (adding every number between 1 and 100): 
total = 0
for number in range(1, 101):
    total += number
print(total)

# How to add all even numbers in a range:
total = 0
for number in range(0,101,2):
    total += number
print(total)

#FizzBuzz in Python. Use remainder (% = 0 is fully divisible, remainder = 1 is not fully divisible --> floats)

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# Password Generator:

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = [] #Start with blank password list


for char in range(1, nr_letters +1): #Takes the number of imputs and directs the variable below to use this value as the number of letters to grab.
    random_char = random.choice(letters)
    password.append(random_char) #adds the above choice in random letters to the previously blank password.

#Rinse and repeat for the other lists:

for char in range(1, nr_symbols +1):
    random_char = random.choice(symbols)
    password.append(random_char)

for char in range(1, nr_numbers +1):
    random_char = random.choice(symbols)
    password.append(random_char)

random.shuffle(password) #Randomize the order of letters, numbers, and symbols in order to make the password more secure.

# Turn the password into a string:
string_password = ""
for char in password:
    string_password += char

print("The password is " + string_password)





