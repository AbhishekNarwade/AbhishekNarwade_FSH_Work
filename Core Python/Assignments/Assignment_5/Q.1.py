# 1. Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

userid = 'admin'
password = 'admin123'
attempts = 3
i = 0
while i < attempts:
    user_input = input("Enter User ID: ")
    pass_input = input("Enter Password: ")
    
    if user_input == userid and pass_input == password:
        print("Login successful!")
        break
    else:
        print("Incorrect User ID or Password. Please try again.")
        i += 1
