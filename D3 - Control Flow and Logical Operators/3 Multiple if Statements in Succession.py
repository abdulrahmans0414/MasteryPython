# multiple if Condition

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height>=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age ?"))
    if age <12 :
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
        
    wantsPhoto =  input("Do you want a phote taken? (y/n): ")
    if wantsPhoto == "y":
        # add $3 their bill
        bill += 3
        print(f"your final bill is $ {bill} ")
    if wantsPhoto == "n":
        print(f"your final bill is ${bill} ")
else:
        print("Sorry, You have to grow taller before you can ride.")
