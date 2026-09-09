# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

def armstrong():
    num = int(input('enter the number :'))
    temp = num
    count = 0
    while temp > 0:
            count +=1
            temp = temp // 10
    
    temp = num
    sum = 0
    while temp > 0:
            d = temp % 10
            sum = sum + (d**count)
            temp = temp // 10
    
    if num == sum:
            return f'{num} is armstrong'  
    
    return(f'{num} is not armstrong')
result = armstrong()
print(result)
