# 10. Write a program to check if entered year is a leap year or not.

def leap_year(year):
    if year % 4 == 0:
        return f'{year} is a leap year'
    return f'{year} is not a leap year'
year = int (input('enter the year : '))
rea = leap_year(year)
print(rea)