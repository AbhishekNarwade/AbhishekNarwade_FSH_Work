#4. WAP to print Armstrong number within a given range

num = int(input("Enter the number: "))
temp = num
count = 0
while temp > 0:
   
    count += 1
    temp = temp // 10
    

    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        temp //= 10
        sum += digit ** count
        

        if sum == num:
            print(f"{num} is an Armstrong number")
        else:
            print(f"{num} is not an Armstrong number")    