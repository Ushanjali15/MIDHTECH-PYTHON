def student_details(name,course):
    print("student name is",name)
    print("student course is",course)


    student_details("usha", "Computer Science")
    student_details("vayug", "Information Technology")
    student_details("alice", "Mathematics")







#using parameters
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
def add(a,b):
    result = a+b
    return result
print(add(a,b))