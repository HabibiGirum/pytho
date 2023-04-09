import math

def approximate_euler(n):
    e = 1
    factorial = 1
    for i in range(1, n):
        factorial *= i
        e += 1 / factorial
    return e

n = int(input("Enter the number of terms to use for approximation: "))
e_approx = approximate_euler(n)
print("Approximation of e using", n, "terms:", e_approx)
