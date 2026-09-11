# Dictionary in python
#  dictionary is a build-in data type that used to store data in key-value pairs. It is mutable and unordered.


info = {
  "name": "Mahreen",
  "age": 19,
  "city": "Kasur"
}

print(info)
print(type(info))


print(info["name"])  # Output: Mahreen

info["name"] = "Yasir" # Updating the value of the key "name"

# Nested Dictionaries
student = {
  "name": "Mahreen",
  "age": 19,
  "subjects": {
    "physics": 90,
    "maths": 95,
    "chemistry": 85
  }
}

print(student)
print(student["subjects"]["maths"])  # Output: 95