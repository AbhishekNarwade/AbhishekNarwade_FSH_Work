# 8. Write a program to prompt user to enter userid and password. After verifying
# the userid and password, prompt user to enter captcha. If captcha is correct, print
# "Login successful", otherwise print "Invalid captcha". If userid or password is
# incorrect, print "Invalid user ID or password".

user_id = input("Enter your user ID: ")
password = input("Enter your password: ")
captcha = input("Enter the captcha: ")
if user_id == "1234" and password == "5678"  :
    if captcha == "ABCD":
        print("Login successful.")
    else:
        print("Invalid captcha.")
else:
    print("Invalid user ID or password.")