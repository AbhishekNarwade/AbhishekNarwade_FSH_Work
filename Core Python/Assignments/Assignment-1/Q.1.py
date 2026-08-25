# 1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

sub1 = int(input('Subject 1 marks: '))
sub2 = int(input('Subject 2 marks: '))
sub3 = int(input('Subject 3 marks: '))
sub4 = int(input('Subject 4 marks: '))
sub5 = int(input('Subject 5 marks: '))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100
print(f'percentage of five sub is : {percentage}')