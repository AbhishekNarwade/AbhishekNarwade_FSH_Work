# 2. Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.

student = int(input("Enter number of students: "))
while student > 0:
    total_marks = 0
    for i in range(1,6):
        marks = float(input(f"Enter marks for subject {i}: "))
        total_marks += marks
    percentage = (total_marks / 500) * 100
    print(f"Percentage for student {student}: {percentage:.2f}%")
    student -= 1