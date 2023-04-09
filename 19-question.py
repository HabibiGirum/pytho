
# loop through the years from 2001 to 2100
for year in range(2001, 2101):
    # check if the year is a leap year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        # print the year followed by a space
        print(year, end=' ')
        # check if we have printed ten years already
        if (year - 2000) % 10 == 0:
            # print a newline character to start a new line
            print()
