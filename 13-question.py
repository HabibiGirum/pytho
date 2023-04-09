# write a program that reverses the digits 
# of a given positive integer number entered 
# from the keyboard.

num = int(input("Enter a positive integer number"))

reverse_number = str(num)[::-1]
reverse_number = int(reverse_number)
print(reverse_number)