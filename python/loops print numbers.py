

for i in range(1, 7):
    print(i)

#new program
rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))
symbol=input("Enter symbol to print:")
for i in range(rows):
    for j in range(cols):
        print(symbol, end=" ")
    print()