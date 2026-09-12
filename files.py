# Files I/O in Python

file = open("demo.txt", "r") # Open a file in read mode
content = file.read() # Read the content of the file
print(content) # Print the content of the file
file.close() # Close the file

# Open a file in write mode
file = open("demo.txt", "w") # Open a file in write mode
file.write("Hello, World!") # Write to the file
file.close() # Close the file

# Open a file in append mode
file = open("demo.txt", "a") # Open a file in append mode
file.write("\nThis is an appended line.") # Append to the file
file.close() # Close the file

