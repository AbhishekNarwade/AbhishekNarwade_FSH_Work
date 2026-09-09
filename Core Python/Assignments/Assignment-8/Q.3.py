# a. 1+ 2 + 3 + 4+..... + n

'''def a(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum +i
    return sum
n = int(input('enter the number :'))    
res = a(n)
print(res)       
'''
# b. 1!+ 2! + 3! + 4!+..... + n!

'''def a():
    sum = 0
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
        sum = sum + fact
    return sum
n = int(input('enter the number :'))    
res = a()
print(res)     '''

#c. 1^1 + 2^2 + 3^3+ ...... n^n

def a():
    sum = 0
    for i in range(1, n+1):
        z = i ** i
        sum = sum + z
    return sum    


    
n = int(input('enter the number :'))    
res = a()
print(res)
