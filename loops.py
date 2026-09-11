# loops in python
# Loops are used to execute a block of code repeatedly until a certain condition is met. Python provides two main types of loops: for loops and while loops.

# while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1  # Increment the count by 1



# Examples of while loop
# Example 1: Print numbers from 1 to 5

num = 1
while num <= 5:
    print(num)
    num += 1


# Example 2: Print even numbers from 2 to 10

num = 2
while num <= 10:
    print(num)
    num += 2



# for loop
for i in range(1, 6):
    print(i)


# Examples of for loop
# Example 1: Print each character in a string

for char in "Hello, World!":
    print(char)


# Example 2: Print each item in a list

for item in ["apple", "banana", "cherry"]:
    print(item)



# Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")