# 4. Write a program to enter P, T, R and calculate simple Interest.

P = int(input('enter the value of P : '))
T = int(input('enter the value of T : '))
R = int(input('enter the value of R : '))

simple_Interest = (P * R * T)/ 100

print(f'simple_Interest is : {simple_Interest}')