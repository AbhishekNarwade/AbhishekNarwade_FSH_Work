# 1. Write a program to find the area and perimeter of following figure (Accept the
   #length, breadth and radius from user:

length = float(input('enter the length  ; '))
breadth = float(input('enter the breadth  ; '))
radius = float(input('enter the radius  ; '))

area_rec = (length * breadth) 
area_cir = (3.14 * radius**2)/2
total_area = area_rec + area_cir

peri_rec = (2* length) + breadth
peri_cir = 3.14 * radius
total_peri = peri_rec + peri_cir

print(f'area of fig is {total_area}')
print(f'perimeter of fig is {total_peri}')