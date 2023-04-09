

def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)


n= int(input("Enter a number that you want to factorial: \n"))
result=factorial(n)
print(result)

