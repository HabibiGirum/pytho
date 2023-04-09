num_students = int(input("Enter the number of students: "))

max_score = -1
max_student = ""

for i in range(num_students):
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    
    if score > max_score:
        max_score = score
        max_student = name
        
print("The student with the highest score is:", max_student)
