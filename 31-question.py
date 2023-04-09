# Define the starting and ending characters
start = ord('!')
end = ord('~')

# Loop through the ASCII characters from start to end
for ascii_code in range(start, end+1):
    # Convert the ASCII code to a character
    char = chr(ascii_code)
    # Print the character, followed by a space
    print(char, end=' ')
    # Check if we have printed ten characters
    if (ascii_code - start + 1) % 10 == 0:
        # If so, print a newline character to start a new line
        print()
