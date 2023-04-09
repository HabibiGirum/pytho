def find_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_perfect(n):
 
    divisors = find_divisors(n)
    if sum(divisors) == n:
        return True
    else:
        return False


n = int(input('Enter a number :\n'))
if is_perfect(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")

# Print all proper divisors of the number
divisors = find_divisors(n)
print(f"Proper divisors of {n}: {divisors}")
