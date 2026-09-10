# A build-in data type that stores sets of values
# it can store elememts of diff types like intm, float, strings etc.

marks = [94.4, 87.5, 92.3, 88.9] #list of float values
print(marks)
print(type(marks))


print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])



#  lists are mutuable but strings are immutable in python 

student = ["Mahreen", 96.7, 19, "BSCS"]
print(student)


# list slicing
print(student[0:2])

# list methods:
student.append("CS")  # adds an element at the end
print(student)



marks.sort()  # sorts the list in ascending order
print(marks)

marks.sort(reverse=True)  # sorts the list in descending order
print(marks)

marks.reverse()  # reverses the list
print(marks)