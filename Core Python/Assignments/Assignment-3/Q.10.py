# 10. Write a program to check if person is eligible to marry or not (male age >=21 and
# female age >=18).


gender = input("Enter your gender (M/F): ")
age = int(input("Enter your age: "))

if (gender == "F" or gender == "f"):
    if age >= 18:
        print("Female is eligible for marriage.")
    else:
        print("Female is not eligible for marriage.")
elif (gender == "M" or gender == "m"):
    if age >= 21:
        print("Male is eligible for marriage.")
    else:
        print("Male is not eligible for marriage.")