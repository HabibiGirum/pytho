# write a program that displays the maximum and 
# the minimum of a list of numbers entered from 
# the keyboard. where the size of the list is 
# to be entered from the keyboard.

size = int(input("Enter the size of the list:"))
list = []

for i in range(size):
    num = float(input(f"Enter the {i+1} number:"))
    list.append(num) #append() is a method that is used to 
    #add an item to the end of a list.
print("From ",list,"The maximum number is:", max(list))
print("From ",list,"The minimum number is:", min(list))
