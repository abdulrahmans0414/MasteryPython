'''
Instructions
This program takes two inputs. 
The first input is stored in a variable called a. 
The second input is stored in a variable called b.

Write a program that switches the values stored in the variables a and b.

Example Input 1
29
41
Example Output 1
a: 41
b: 29
Example Input 2
Hello
World
Example Output 2
a: World
b: Hello

'''
# There are two variables, a and b from input
a = input()
b = input()

# Switching the values of a and b using a temporary variable
temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)

