# Q.7 Find the sum of three-digit number.

'''first_digit = int(input('Enter the first digit : '))
sec_digit = int(input('Enter the second digit : '))
third_digit = int(input('Enter the third digit : '))

sum = first_digit + sec_digit + third_digit

print(f'the sum of three-digit number is {sum}')''' 

"""three_digit_number = int(input('enter the three-digit number : '))

a = (three_digit_number // 100)    #1 
b = (three_digit_number // 10) % 10  #2
c = three_digit_number % 10    #3

sum = a + b + c 

print(f'the sum of three-digit number is {sum}')"""


four_digit_number = int(input('enter the four-digit number : '))

a = (four_digit_number// 1000)    #1 
b = (four_digit_number // 100) % 10  #2
c = (four_digit_number // 10) % 10 #3
d = four_digit_number % 10
sum = a + b + c + d

print(f'the sum of four-digit number is {sum}')