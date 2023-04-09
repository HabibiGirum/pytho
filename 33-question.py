rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1):
    for j in range(rows-i):
        print(" ", end="")
    for k in range(i, 0, -1):
        print(k, end=" ")
    for l in range(2, i+1):
        print(l, end=" ")
    print()
