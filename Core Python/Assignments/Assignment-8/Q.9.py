#9. Write a program to check if entered number is a palindrome or not using function.

def palli(num):
    temp = num
    rev = 0
    while (temp> 0):
        d = temp % 10
        rev = rev * 10 + d
        temp = temp // 10
    if (num == rev):
        return f"{num} is Palindrome"
    else:
        return f"{num} is Not a Palindrome"
num = int(input('Enter the number : '))    
res = palli(num)
print(res)    
