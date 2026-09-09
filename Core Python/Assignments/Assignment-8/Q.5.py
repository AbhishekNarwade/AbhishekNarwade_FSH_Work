
# 5. Sum of all prime numbers between 1 to n 
def prime():
    sum = 0
    for i in range(2, num):
        if num % i != 0:
            return i
    if prime():
        sum = sum + i
    return sum     
    
num = int(input('enter the umber :')) 
res = prime()
print(res)  