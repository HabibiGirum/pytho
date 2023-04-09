max = count = 0

while True:
    num = int(input("Enter an integer (0 to end): "))
    if num == 0:
        break
    if num > max:
        max = num
        count = 1
    elif num == max:
        count += 1

print(f"The max integer is {max} and it occurs {count} times.")
