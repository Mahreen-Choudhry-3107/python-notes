# Conditional Statements in Python

# if-elif-else(SYNTAX)
"""
if(condition):
    Statement1
elif(condition):
    Statement2
else:
    StatementN

"""

# Example 1: Check if a number is positive, negative or zero
num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive.")
elif num < 0:
    print("Number is negative.")
else:
    print("Number is zero.")


# AND, OR, Not Operators in Python

# AND Operator
a = 5
b = 10

if a > 0 and b > 0:
    print("Both numbers are positive.")
    
# OR Operator
c = 5
d = -10

if c > 0 or d > 0:
    print("At least one number is positive.")

# Not Operator
e = 5

if not e < 0:
    print("Number is not negative.")





# Clever if-else statement in python

x = 10
print("x is positive.") if x > 0 else print("x is not positive.")

# Problem => Check if a person is eligible to vote or not
age = int(input("Enter your age: "))
vote = ("yes", "no") [age >= 18]