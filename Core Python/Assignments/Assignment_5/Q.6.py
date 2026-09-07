# 6. Write a program to print first n prime numbers.

n = int(input("Enter the number of prime numbers to print: "))
if n > 0:
    for i in range(2, n +1):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i) 