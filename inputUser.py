from math import *

# Working with strings
the_DarkKnight = "Batman"
print("Here is the \"" + the_DarkKnight.upper() + "\"")
print(the_DarkKnight.index("a"))
print(the_DarkKnight.replace("Batman", "Abel"))

print("======================================")
# Working with numbers
print(10 % 3) # modulus which is 10 divided by 3 is 9, which the 1 is the mod
myNum = 69
print(str(myNum) + " is my favorite number uhuhuh") #printing out number as a string

# Building a simple calculator
print("======================================")
number1 = input("Enter number: ")
number2 = input("Enter second number: ")
result = float(number1) + float(number2)
print(result)

# Asking user input
print("======================================")
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + ", I see that your age is " + age)

# Making a list
print("======================================")
friends = ["Jacob", "Viejo", "Tommy", "Alan"] # or {}
print(friends[1:]) # To specify a range
print(friends[1:3]) # More specific

