'''A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
cost of fencing the field.'''

rad = 20
leng = 50
brea = 40

pi = 3.13

# Perimeter of semicircle (curved part)
semi_circum = pi * rad

# Remaining 3 sides of rectangle
rect_side = leng + leng + brea

# Total perimeter
perimeter = semi_circum + rect_side

# Fencing 5 times
total_wire = perimeter * 5

total_cost = total_wire * 35

print("Total cost =", total_cost)