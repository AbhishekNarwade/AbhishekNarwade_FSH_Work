# 6. WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

basic = float(input('enter the basic salary : '))

da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

total_salary = da + ta + hra + basic

print('da',da)
print('ta',ta)
print('hra',hra)
print(f' total salary of employee based on basi is : {total_salary}')