# Functions in python 

# A function is a block of code that is designed to perform a specific task. It can take inputs, process them, and return an output. Functions help in organizing code, making it reusable, and improving readability.


# Example of a simple function
def greet():
    print("Hello, welcome to Python functions!")


# Calling the function
greet()  # Output: Hello, welcome to Python functions!



# function with parameters
# sum of two numbers
def sum_two_numbers(a, b):
    return a + b


# Calling the function with arguments

result = sum_two_numbers(5, 10)
print("Sum:", result)  # Output: Sum: 15



# function with default parameters
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()  # Output: Hello, Guest!



greet_user("Mahreen")  # Output: Hello, Mahreen!

name = input("Enter your name: ")
greet_user(name)  # Output: Hello, <name>! (where <name> is their input)

