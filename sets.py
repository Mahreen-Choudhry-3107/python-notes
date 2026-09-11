# Sets in Python
# sets are collections of unique elements. They are unordered, meaning that the items do not have a defined order, and they do not allow duplicate values.

nums = {1, 2, 3, 4, 5}

print(nums)
print(type(nums))

collections = {"apple", "banana", "cherry", "date", 1, 3, 2, 2, 2}
print(collections)

print(len(collections))  # Output: 7, because duplicate values are not counted

# empty set
empty_set = set() # set is mutable but elements inside it must be immutable (like numbers, strings, tuples)

# set methods
empty_set.add(10)
empty_set.add(20)
print(empty_set)  # Output: {10, 20}

empty_set.remove(10)
print(empty_set)  # Output: {20}

empty_set.clear() # Removes all elements from the set

print(empty_set)  # Output: set()

collections.pop()  # Removes and returns an arbitrary element from the set
print(collections)  # Output: The set without the popped element