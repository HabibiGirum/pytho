# there are two method to do this problem 
#1. using by import math module 
import math
n = int(input('enter the value of x'))
print(f"Using math.exp: {math.exp(n)}")

#2. the second method using such expirations
def infinite_series_expansions(x,n_terms):
    result =1
    term =1
    for i in range(1,n_terms):
        term *= x/i
        result +=term
    return result

# input from user

x = int(input('enter the value of x'))
n_terms = int(input('enter the number of terms to add'))

print(f"e^{x} = {infinite_series_expansions(x, n_terms)}")
