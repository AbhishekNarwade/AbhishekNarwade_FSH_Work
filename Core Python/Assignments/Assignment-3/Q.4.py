# 4. Write a program to input all sides of a triangle and check whether triangle is valid or
# not.

side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")