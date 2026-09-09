'''1. Write a program to calculate area of rectangle'''

'''def area_rect(length, breath):
    area = length * breath
    print(area)
area_rect(10, 20)   ''' 


'''def area_rect():
    length = int(input('enter the length :'))
    breath = int (input('enter the breath :'))
    area = length * breath
    print(area)
area_rect()  ''' 


'''def area_rect():
    length = int(input('enter the length :'))
    breath = int (input('enter the breath :'))
    area = length * breath
    return area
res = area_rect()
print(res)  '''


def area_rect(length, breath):
    
    area = length * breath
    return area

res = area_rect(10, 20)
print(res)  
