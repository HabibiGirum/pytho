def factorial(n):
    """
    This function computes the factorial of a given integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def series_sum(n):
    """
    This function computes the sum of the series 1! + 2! + 3! + ... + n!.
    """
    sum = 0
    for i in range(1, n+1):
        sum += factorial(i)
    return sum

n = int(input("Enter a positive integer: "))
print("The sum of the series is:", series_sum(n))
