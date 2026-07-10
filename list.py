student_marks=[70,85,90]
total=sum(student_marks)
average=total/len(student_marks)

print("average marks:",average)







#list and its methods

fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

# append()
fruits.append("Orange")
print("After append:", fruits)

# insert()
fruits.insert(1, "Grapes")
print("After insert:", fruits)

# extend()
fruits.extend(["Pineapple", "Kiwi"])
print("After extend:", fruits)

# remove()
fruits.remove("Banana")
print("After remove:", fruits)

# pop()
fruits.pop()
print("After pop:", fruits)

# index()
print("Index of Mango:", fruits.index("Mango"))

# count()
print("Count of Apple:", fruits.count("Apple"))

# sort()
fruits.sort()
print("After sort:", fruits)

# reverse()
fruits.reverse()
print("After reverse:", fruits)

# copy()
new_list = fruits.copy()
print("Copied List:", new_list)

# clear()
new_list.clear()
print("After clear:", new_list)