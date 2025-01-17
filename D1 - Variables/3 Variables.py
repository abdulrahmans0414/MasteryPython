# pyhthon variables
# Learn to store values in containers for later use. Variables is a concept in programming that allows us to give a label to a piece of data so that we can refer or reference that data using the chosen variable name. We will see in this lesson how to create variables and how to use the variables to access the contained value.

name = "Abdul"
print(name)

name ="Rahman"
print(name)


# print(len (input("What is your name ?")))
name = input("What is your name?")
length = len(name)
print(length)


"""
Variables
We have 2 variables glass1 and glass2. glass1 contains milk and 
glass2 contains juice. Write 3 lines of code to switch the contents of the variables. 
You are not allowed to type the words "milk" or "juice". 
You are only allowed to use variables to solve this exercise.
"""

glass1 = "milk"
glass2 = "juice"

temp = glass1
glass1 = glass2
glass2 = temp