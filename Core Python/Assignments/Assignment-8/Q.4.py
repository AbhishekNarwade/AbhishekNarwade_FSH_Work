# 4. Sum of all odd numbers between 1 to n

def odd():
    sum = 0
    for i in range(1, n+1, 2):
            sum = sum + i
    return sum
n = int(input('enter the umber :')) 
res = odd()
print(res)       
