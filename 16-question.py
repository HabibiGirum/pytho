# write a program to sum the following series:

# 1/3 + 3/5 + 7/9 +9/11 + 11/13 + ... + 95/97 + 97/99

numerator= 1
denominator = 3

sum = 0

while numerator<=95:
    sum+=numerator / denominator
    numerator += 2
    denominator +=2

print("the sum of the series is : ", sum , " or ", numerator ,"/",denominator)
