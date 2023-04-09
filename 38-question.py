def isPrime(num):
    if num < 2:
        return print('Not prime number')
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return print('no',num,",is no prime number")
    return print('Yes ,', num ,' this is prime number')

n=int(input('Enter a number '))
isPrime(n)
