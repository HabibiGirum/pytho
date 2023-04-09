def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")










def sum_of_digits(n):
    if n < 0:
        n = -n
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum

num = int(input("Enter a number: "))
digit_sum = sum_of_digits(num)
print("The sum of digits of", num, "is", digit_sum)
