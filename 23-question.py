def is_prime(n):
    """
    This function takes an integer n as input and returns True if it is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):

        if n % i == 0:
            return False
    return True


def count_primes(n):
    """
    This function takes an integer n as input and returns the number of primes between 2 and n (inclusive).
    """
    count = 0
    for i in range(2, n+1):
        if is_prime(i):
            count += 1
    return count


# Test the function with input N=100
print(count_primes(100))
print(count_primes(10000))
