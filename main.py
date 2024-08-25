# Data Types
# Integer --- whole number
# Float --- decimal number
# String --- text
# Boolean --- True or False

# Printing to console
# Print Function
# print("Hello World")

# print("Hello World\n", "Hello World\n", "Hello World\n")
# for i in range(1,11):
#   print("Hello World")

# # Print a recipe
# print("1. mix 500g of flour, 10g yeast and 300ml water in a bowl")
# print("2. knead the dough for 10 minutes")
# print("3. place the dough in a lightly oiled bowl and cover with a clean cloth")

# print("1. mix 500g of flour, 10g yeast and 300ml water in a bowl\n"
  # "2. knead the dough for 10 minutes\n"
  # "3. place the dough in a lightly oiled")

# print(" i would've played yesterday")

# def my_var():
#   print("Hello World")
# my_var()

# def my_var2():
#   print("1st python session")
# my_var2()

# def my_var3():
#   print("1st python session\n2nd python session")
# my_var3()

# String Manipulation
# print("Hello" + " " + "World")
# print("Hello" + " World")


# name = input("What is your name?")

# name = input("What is your name?")
# # print(name)

# print("My name is" + " " + name)

# name = print(len(input("What is your name? ")))

# name = input("What is your name? ")
# length = len(name)
# print(length)

# Band Name Generator

# print("Welcome to the Band Name Generator")
# name = input("Name of city ")
# pet = input("Name of pet ")
# print("Your band name is" + " " + name + " " + pet)

# print("Welcome to the Band Name Generator")
# city = input("Name of city ")
# pet = input("Name of pet ")
# print(f"Your band name is {city} {pet}")

# Variables
# subscripting
# print("hello"[1])
# print(123 + 345)
# print("123"+"456")


# num_char = str(len(input("What is your name? ")))
# print("Your name has " + num_char + " characters")


# a= float(3.14159)
# b= int(1.99)
# print(a)
# print(b)


# var = input("Enter three digits: ")
# print(var[0])
# print(var[1])
# print(var[2])


# print(3 + 4)
# print(3 - 4)
# print(3 * 4)
# print(3 / 4)
# print(3 ** 4)

# Tip Calculator
# welcome
# Bill
# People
# Tip
# Tip/ 100
# Tip - Bill
# Bill/People
# Display
print("Welcome to the tip calculator")
bill = int(input("Enter bill amount $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What tip would you like to give? 10, 12, or 15? "))
tip_percent = int(tip)/100
tip_amount = int(bill) * int(tip_percent)
total_bill = int(bill) + int(tip_amount)
bill_per_person = int(total_bill)/int(people)
print(f"Each person should pay: ${bill_per_person}")










