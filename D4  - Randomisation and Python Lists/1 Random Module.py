# random module

import random
import my_module 

# random interger number 
random_integer = random.randint(0,10)
print (random_integer)

# import from my_module module 
print(my_module.pi)

# random float numbers 0.00000000 -0.99999999...
random_float = random.random()
print (random_float)

# how to create a random number decimal number between 0 and 0 and 5?
# answer 0.00000... - 4.99999...
random_float = random.random() * 5
print (random_float)

love_score = random.randint(1,100)
print (f"Your love score is {love_score}")
