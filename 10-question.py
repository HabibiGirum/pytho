def count_passing(marks):
    count = 0
    for mark in marks:
        if mark > 20:
            count += 1
    return count

num_students = int(input("Enter the number of students who took the test: "))
marks_list = input("Enter the marks of the students separated by spaces: ")
marks_list = marks_list.split()
marks_list = [int(mark) for mark in marks_list]

passing_count = count_passing(marks_list)

print("Out of", num_students, "students who took the test,",
      passing_count, "students scored greater than 20 out of 30.")
