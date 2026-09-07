# 5. Write a program to print prime numbers between 1 to 100.

num = int(input("Enter the number: "))
if num > 1:
    for i in range( 2,num):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")