# String is a data type in Python that represents a sequence of characters. Strings are used to store and manipulate text-based data. In Python, strings can be defined using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).

str1 = 'Hello, World!'  # Using single quotes
str2 = "Python is awesome!"  # Using double quotes
str3 = '''This is a multi-line string.'''  # Using triple quotes

# Concatenation:

# Strings can be concatenated using the + operator
greeting = str1 + " " + str2


# Strings can be repeated using the * operator
repeated_greeting = str1 * 3

# length of strings:

name = "Mahreen"
print(len(name)) # Output: 7


# Indexing 
# starts from 0 and goes up to n-1, where n is the length of the string
#  we can only access characters in string but we cannot modify them because strings are immutable in Python.


print(name[0])  # Output: M
print(name[6])  # Output: n


# Slicing

print(name[1:5])  # Output: ahre


# negative indexing

print(name[-1])  # Output: n
print(name[-7])  # Output: M

# String Functions:

# Returns True if the string ends with '!', otherwise False
print(str3.endswith('!'))  # Output: False
print(str2.endswith('!'))  # Output: True

# str.capitalize()  # Returns a copy of the string with the first character capitalized and the rest lowercased

print(name.capitalize())  # Output: Mahreen

print(name.replace('M', 'm'))  # Output: mahreen

print(name.find('h'))  # Output: 2

print(name.count('e'))  # Output: 2

