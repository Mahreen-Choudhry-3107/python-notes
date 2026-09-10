# This is a simple Python script

name = input("Enter your name: ")
print("Welcome", name, "!")

age = input("Enter your age: ")
print("You are", age, "years old.")

age_number = int(input("Enter your age as a number: "))
print("Next year you will be", age_number + 1)

height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

first_name, last_name = input("Enter your first and last name: ").split()
print("Your full name is", first_name, last_name)

favorite_color = input("Enter your favorite color: ")
print("Your favorite color is", favorite_color)

answer = input("Do you like Python? (yes/no): ").lower()
if answer == "yes":
	print("Great choice!")
else:
	print("You may like it more with practice.")
