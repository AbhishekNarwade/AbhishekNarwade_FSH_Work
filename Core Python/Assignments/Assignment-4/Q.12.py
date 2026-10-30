# 12. Write a program to check if given number is Armstrong number or not.
cnum = int(input("Enter a number: "))
temp = cnum
count = 0
while temp > 0:
    count += 1
    temp //= 10

temp = cnum
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** count
    temp //= 10

if sum == cnum:
    print(f"{cnum} is an Armstrong Number.")
else:
    print(f"{cnum} is not an Armstrong Number.")