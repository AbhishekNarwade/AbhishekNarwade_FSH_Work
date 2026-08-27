# 5. WAP to print fibonic series till n numbers.

num = int(input('enter the number till you want fibonic series :'))
a = -1
b =1
for i in range (num):
    c = a + b
    print(c, end = '_')
    a = b
    b = c