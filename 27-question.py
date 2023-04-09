print("Welcome to the unit converter program!")

while True:
    print("\nWhat would you like to convert?")
    print("1. Kilograms to Pounds")
    print("2. Miles to Kilometers")
    print("3. Hours to Minutes")
    print("4. Quit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(kg, "kilograms is equal to", pounds, "pounds.")
        
    elif choice == "2":
        miles = float(input("Enter distance in miles: "))
        km = miles * 1.60934
        print(miles, "miles is equal to", km, "kilometers.")
        
    elif choice == "3":
        hours = float(input("Enter time in hours: "))
        minutes = hours * 60
        print(hours, "hours is equal to", minutes, "minutes.")
        
    elif choice == "4":
        print("Thank you for using the unit converter program!")
        break
        
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
