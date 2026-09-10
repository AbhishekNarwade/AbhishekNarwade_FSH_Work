num = int(input('Enter the three digit number : '))

'''num = int(input("Enter a 3-digit number: "))

count = 1

while count <= 3:
    d1 = num % 10
    num = num // 10

    if count == 1:
        third = d1
    elif count == 2:
        second = d1
    else:
        first = d1

    count = count + 1

if first == 2 * second and first == third / 2:
    print("Yes, you have done it")
else:
    print("Please try next time")
'''
d1 = num % 10
num = num // 10

d2 = num % 10
num = num //10

d3 = num % 10


if d3 == 2*d2 and d3==d1/2 :
    print('Yes, you have done it')
else:
    print('pleas, try again')    


