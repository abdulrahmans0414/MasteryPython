"""
Instructions
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Example 1 Input
39

Example 1 Output
12
Example 2 Input
43

Example 2 Output
7

"""

# Take a two-digit number as input
two_digit_number = input("Enter 2 digit number")

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# add the two integers together
two_digit_number = first_digit + second_digit

print(two_digit_number)