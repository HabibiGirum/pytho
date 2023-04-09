def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    else:
        return a / b

print("Welcome to the calculator program!\n")

while True:
    print("Please select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("\nThank you for using the calculator program!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(num1, "+", num2, "=", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print(num1, "-", num2, "=", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print(num1, "*", num2, "=", result)
    elif choice == '4':
        result = divide(num1, num2)
        print(num1, "/", num2, "=", result)
    else:
        print("Invalid choice. Please try again.\n")
