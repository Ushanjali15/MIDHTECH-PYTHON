# Find maximum and minimum using only if statements

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Maximum value =", num1)

if num2 > num1:
    print("Maximum value =", num2)

if num1 < num2:
    print("Minimum value =", num1)

if num2 < num1:
    print("Minimum value =", num2)

if num1 == num2:
    print("Both numbers are equal.")


