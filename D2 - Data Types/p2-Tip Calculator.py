# if the bill was $150.00 , split between 5 people , with 12% tip.
# Each person should pay (150/5) * 1.12
# round the result to 2 decimal places = 33.60

# welcome to the tip claculatro.
# What was teh total bill ? $124.56
# What percentage tip would you like to give ? 10, 12,or 15 ? 12
# How many people to split the bill ? 7
# Each person should pay : $19.93

print("Welcome to the tip Calculator!")
# totalBill = input("What was the total bill ? $ ")
# print(type(totalBill)) data type is string

# change in float
totalBill = float(input("What was the total bill ? $ "))

tip = int(input("How much tip would you like to give ? 10, 12, or 15 ?"))

people = int(input("How many people split the bill ? $ "))

totalBillWithTip = tip /100 * totalBill + totalBill
print(totalBillWithTip)

totalBillPerPerson = totalBillWithTip / people
finalAmount =round(totalBillPerPerson,2)

finalAmount ="{:.2f}".format(totalBillPerPerson)
print(f"Each person should pay $ {finalAmount}")