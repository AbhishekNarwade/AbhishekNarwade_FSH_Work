#7. Write a program to find sum of digits of a number.

def sum_of_digits(num):
    temp = num
    sum = 0
    while temp >0:
        d = temp % 10
        sum = sum + d
        temp = temp // 10
    return sum
result = sum_of_digits(int(input("Enter the number: ")))
print(f"Sum of digits of {result} is: {result}")