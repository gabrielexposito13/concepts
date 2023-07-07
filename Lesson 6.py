#Lesson 6
import random
#Built-in functions examples:
print()
len()

#Create new function:

def my_function():
    print("Hello")
    print("Bye")

#How to call the function:

my_function()


# Defining a function combines other functions for a new purpose.
# Example of a function that finds the minimum value and then adds the maximum:

r_list = []
for i in range(0,100):
    r_list.append(random.randint(0,1000))

def min_max():
    a = min()
    b = max()
    a+b

min_max(r_list)
print(min_max)
