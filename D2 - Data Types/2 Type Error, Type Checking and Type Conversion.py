# Type error , type checking and type conversion

# TypeError
# len(123)

# No TypeError
len("Hello")

# Type checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# example
a = 123
print(type(a))


# Type Conversion
str()
int()
float()
bool()

# example
a=str(123)
print(type(a))

a=float(123)
print(type(a))

# print(70 + float("100.5"))
print(str(70)+ str(100))



name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int

print("Number of letters in your name: " + str(length_of_name))