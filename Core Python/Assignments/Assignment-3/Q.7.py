# 7. Write a program to check if user has entered correct userid and password.

user_id = input("Enter your user ID: ")
password = input("Enter your password: ")

if user_id == "admin" and password == "password":
    print("Login successful.")
else:
    print("Invalid user ID or password.")