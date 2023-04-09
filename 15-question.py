# 15. write a program that searches for the 
# least common multiple(LCM) of two natural numbers.


import math

num1= int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm=math.lcm(num1,num2)
print("The LCM of", num1, "and", num2, "is", lcm)
