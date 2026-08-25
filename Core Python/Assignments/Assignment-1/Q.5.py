# 5. Write a program to enter P, T, R and calculate Compound Interest.


P = float(input("Enter Principal: "))
T = float(input("Enter Time: "))
R = float(input("Enter Rate: "))

CI = P * ((1 + R / 100) ** T) - P

print(f"Compound Interest = {CI}")