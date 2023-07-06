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





