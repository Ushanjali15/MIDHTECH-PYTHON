numbers={1,2,3,4,5,6, 7,8,9,10,12,13,14,11}
print("basic examples:",numbers)



#program2
courses=["python","java","python","devops","java"]
unique_courses=set(courses)

print("unique courses:",unique_courses)



#program3
A = {50, 60, 70, 80}
B = {30, 40, 50, 60}

print("Set A:", A)
print("Set B:", B)

# Add
A.add(20)
print("After add:", A)

# Update
A.update([80, 90])
print("After update:", A)

# Remove
A.remove(90)
print("After remove:", A)

# Discard
A.discard(80)
print("After discard:", A)

# Pop
x = A.pop()
print("Popped Element:", x)
print("After pop:", A)

# Copy
C = A.copy()
print("Copied Set:", C)

# Union
print("Union:", A.union(B))

# Intersection
print("Intersection:", A.intersection(B))

# Difference
print("Difference (A-B):", A.difference(B))

# Symmetric Difference
print("Symmetric Difference:", A.symmetric_difference(B))

# Intersection Update
D = A.copy()
D.intersection_update(B)
print("Intersection Update:", D)

# Difference Update
E = A.copy()
E.difference_update(B)
print("Difference Update:", E)

# Symmetric Difference Update
F = A.copy()
F.symmetric_difference_update(B)
print("Symmetric Difference Update:", F)

# issubset
print({30, 40}.issubset(B))

# issuperset
print(B.issuperset({30, 40}))

# isdisjoint
print(A.isdisjoint({100, 200}))

# Clear
A.clear()
print("After Clear:", A)
