def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


num = int(input("please give me a positive integer:"))

if num<=0:
    print("please give me a positive integer")
else:
    print("fibonacci series: ")
    for i in range(num):
        print(fibonacci(i),end=',');