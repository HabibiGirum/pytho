print("Welcome to the student score program!")
num_students = int(input("Enter the number of students: "))

# initialize variables for highest and second-highest scores
highest_score = -1
second_highest_score = -1

# initialize variables for names of students with highest and second-highest scores
highest_name = ""
second_highest_name = ""

# loop through each student and get their name and score
for i in range(num_students):
    name = input("Enter the student's name: ")
    score = float(input("Enter the student's score: "))
    
    # update highest and second-highest scores and names
    if score > highest_score:
        second_highest_score = highest_score
        second_highest_name = highest_name
        highest_score = score
        highest_name = name
    elif score > second_highest_score:
        second_highest_score = score
        second_highest_name = name

# print out the results
print("The student with the highest score is", highest_name, "with a score of", highest_score)
print("The student with the second-highest score is", second_highest_name, "with a score of", second_highest_score)
