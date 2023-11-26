# Number Manipulation and F Strings in Python

# float
print(8/3)

# into integer
print(int(8/3))

# round numbers
print(round(8/3))

# the number of digits of prcison you want to round it to
print(round(8/3, 2))

# floor division
print(8 // 3 )
print(type(8 // 3 ))
print(type(8 / 3 ))


# result calculation into a variable
result = 4 / 2

# again devided by 2
result /= 2
print(result)


# User initial score 
score = 0

# user scores a point

# score = score + 1
# same as above
score += 1 
# same i can use -= , *= and /= 

print(score)
print("Your score is " + str(score) )

# F String 
height = 1.8
isWinnig = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinnig}")


