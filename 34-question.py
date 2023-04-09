# Define the number of rows
num_rows = 6

# Loop through each row
for i in range(num_rows):
    # Print the spaces at the beginning of the row
    print(" " * (num_rows - i - 1), end="")
    
    # Loop through each number in the row
    for j in range(i + 1):
        # Calculate the value to print
        value = 2**(j + i)
        
        # Print the value and a space
        print(str(value) + " ", end="")
    
    # Print a new line
    print()
