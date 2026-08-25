# write a python program to check whether male and female are eligible for marriage or not based on their age. The minimum age for female is 18  and for male is 21.

gender = input('Enter the gender (M/F): ')
age = int(input('Enter the age: '))

if(gender == "F"):
    if(age >= 18):
        print("Female is eligible for marriage.")
    else:
        print("Female is not eligible for marriage.")
elif(gender == 'M'):
    if(age >= 21):
        print("Male is eligible for marriage.")
    else:
        print("Male is not eligible for marriage.")
else:
    print("invalid ")        