# Tuples in python
# A build-in data type that let us create immutable sequence of values.


tup = (87, 64, 33, 95, 76)

print(tup)
print(type(tup))

# tup[0] = 100 # This will raise an error because tuples are immutable

# empty tuple
tup1 = ()

tup2 = (1,)  # single element tuple, note the comma

# slicing

print(tup[1:3])  # Output: (64, 33)

print(tup.index(95))  # Output: 3
print(tup.count(76))  # Output: 1