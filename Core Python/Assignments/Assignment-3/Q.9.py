# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))
sub4 = int(input("Enter marks for subject 4: "))
sub5 = int(input("Enter marks for subject 5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5

percentage = (total_marks / 500) * 100

if percentage >= 90:
    print("First class")
elif percentage >= 80:
    print("Second class")
else:
    print("Third class")