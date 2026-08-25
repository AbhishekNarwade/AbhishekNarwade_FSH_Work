# 3. Write a program to accept distance in km and convert it into meters and centimeters both.

km = int (input("Enter distance in kilometers: "))

meters = 100 * km
centimeter = 100000 * km

print(f"meters : {meters}")
print(f'centimeters : {centimeter}')