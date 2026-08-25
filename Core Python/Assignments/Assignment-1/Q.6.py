# 6. Write a Program to input two angles from user and find third angle of the triangle.

angle1 = int(input('Enter the angle1 : '))
angle2 = int(input('Enter the angle2 : '))

third_angle = 180 - (angle1 + angle2)

print(f'third angle of the triangle is : {third_angle}')