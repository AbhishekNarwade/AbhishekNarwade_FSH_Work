# 8. Write a program find reverse of a number

def rev_num (num):
    temp = num
    rev = 0
    while temp > 0:
        d = temp % 10
        rev = rev * 10 + d
        temp = temp // 10
    return rev
result = rev_num(int(input("Enter the number: ")))
print(f"Reverse of {result} is: {result}")