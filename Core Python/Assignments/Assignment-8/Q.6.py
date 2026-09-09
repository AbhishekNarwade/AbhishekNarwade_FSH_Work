#  6. Write a program to find print the following Fibonacci series using
#functions:
#1 1 2 3 5 8 n terms

def faibo():
    n = int(input("Enter the number of terms: "))
    a = -1
    b = 1
    for i in range(0, n):
        print(b, end=" ")
        c = a + b
        a = b
        b = c
    

res = faibo()
print(res)