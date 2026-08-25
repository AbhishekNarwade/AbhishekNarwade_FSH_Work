# 12. Write a program to check if given 3 digit number is a palindrome or not.

number = input("Enter a 3-digit number: ")

if number == number[::-1]:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")