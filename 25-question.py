# Initialize variables to keep track of counts and total
count_positive = 0
count_negative = 0
total = 0

# Keep reading input until 0 is entered
while True:
    # Read an integer from input
    num = int(input("Enter an integer value, the program exits if the input is 0: "))
    
    # Break out of loop if 0 is entered
    if num == 0:
        break
    
    # Count positive and negative values
    if num > 0:
        count_positive += 1
    elif num < 0:
        count_negative += 1
    
    # Add non-zero values to total
    if num != 0:
        total += num


if count_positive + count_negative == 0:
    avg = 0
else:
    avg = total / (count_positive + count_negative)

# Print the results
print(f"The number of positives is {count_positive}")
print(f"The number of negatives is {count_negative}")
print(f"The total is {total}")
print(f"The average is {avg:.2f}")
