def sum_of_cubes(num):
    """
    Returns True if the sum of the cube of the digits of num equals num, False otherwise
    """
    digits = [int(digit) for digit in str(num)]
    sum_of_cubes = sum([digit ** 3 for digit in digits])
    return sum_of_cubes == num

# Prompt the user for the low and high values
low = int(input("Enter the low value: "))
high = int(input("Enter the high value: "))

# Loop through all integers between low and high, and print the ones that satisfy the condition
for num in range(low, high+1):
    if sum_of_cubes(num):
        print(num)
