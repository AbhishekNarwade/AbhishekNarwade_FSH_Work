gender = input('enter the gender : ')
age = int(input('enter the age :'))
if(gender=="F"):
    if(age>=18):
        print("eligible")
    else:
        print("not eligible")    
else:
    if(age>=21):
        print("eligible")
    else:
        print("not eligible")