# Initialize the count and the line variable
count = 0
line = ""

# Loop through the numbers 100 to 200 (inclusive)
for num in range(100, 201):
    # Check if the number is divisible by 5 or 6, but not both
    if (num % 5 == 0 or num % 6 == 0) and not (num % 5 == 0 and num % 6 == 0):
        # Add the number to the line string
        line += str(num) + " "
        count += 1
        
        # Check if we have reached 10 numbers per line
        if count == 10:
            # Print the line and reset the count and line variables
            print(line)
            count = 0
            line = ""
        
# Print any remaining numbers on the last line
if count > 0:
    print(line)
