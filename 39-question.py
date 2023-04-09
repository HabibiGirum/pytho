def isEven(num):
    if num % 2 == 0:
        return print(num, 'is even number')
    else:
        return print(num, 'is not even number')
n= int(input('Enter a number '))
isEven(n)