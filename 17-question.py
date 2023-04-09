def calculate_isbn(isbn):

    # checksum
    checksum = sum([(i + 1)*int(digit) for i, digit in enumerate(str(isbn))])%11

    # if the checksum is 10, use  'X' as the last digit

    if checksum == 10:
        return f"{isbn}X"
    else:
        return f"{isbn}{checksum}"
    
# input from user
first_9_digits = input('Enter the first 9 digits of the ISBN: ')

result = calculate_isbn(first_9_digits)

print(result);