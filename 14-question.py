# write a program that searches for the Greatest 
# Common Divisor(GCD) for two natural numbers.
import math

num1= int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd=math.gcd(num1,num2)
print("The GCD of", num1, "and", num2, "is", gcd)