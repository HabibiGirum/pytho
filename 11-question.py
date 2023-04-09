phone_number = input("Please give me a 9 digit phone number:")
if phone_number.isdigit() and len(phone_number) == 9:
    
    if phone_number.startswith("9"):
        print("mobile")
    else:
        print("fixed phone")
else:
    print("invalid phone number,Please enter only 9 digit number")



