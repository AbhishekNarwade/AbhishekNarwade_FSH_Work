# 9. WAP to print all numbers in a range divisible by a given number.

num = int(input("enter the number :"))
for i in range(1, 101):
    if(i % num == 0):
        print(i)