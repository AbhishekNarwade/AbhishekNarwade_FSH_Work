# 10. Write a program to reverse three-digit number.

rev_no = int(input('Enter the three digit number : '))

a = rev_no // 100
b = (rev_no//10)%10
c = rev_no % 10

num = 100 * c + 10 * b + a

print(f'reverce number is : {num}')