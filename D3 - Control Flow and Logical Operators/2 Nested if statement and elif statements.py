# Nested if statements and elif statements

# nested if /else statements
# in nested if statements passed we check another condition inside if condition


print("Welcome to the Indian Army !")
height = int(input("What is your height in cm ? "))

# condition 
if height >= 170:
    print("You are eligible to join the Indian Army.")
    age = int(input("What is your age ? "))
    if age >= 18:
        print("You are eligible")
    elif age >=16:
        print("you are eligible for Airforce.")
    else:
        print("wait..., now till you are not 18 years old")
else:
    print(" Sorry, You are not eligible to join the Indian Army .")
    

