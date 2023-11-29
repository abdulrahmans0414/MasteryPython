# Check the number is odd or even

"""
Instructions
Write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

e.g. 86 is even because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is odd because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

e.g.

6 ÷ 2 = 3 with no remainder.

therefore: 6 % 2 = 0

5 ÷ 2 = 2 x 2 + 1, remainder is 1.

therefore: 5 % 2 = 1

14 ÷ 4 = 3 x 4 + 2, remainder is 2.

therefore: 14 % 4 = 2

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example 1 Input
43
Example 1 Output
This is an odd number.
Example 2 Input
94
Example 2 Output
This is an even number.

"""

# Which number you want to check?
number =int(input("Write any random number"))

# if the number can be divided by 2 with o remainder.
if number % 2 == 0:
    print("This is an even number .")

# otherwise (number cannot be divided by 2 with o remainder).
else:
    print("This is an odd number .")