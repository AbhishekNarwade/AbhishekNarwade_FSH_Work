# 11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount = int(input('Enter the amount : '))


rs500 = amount // 500
amount = amount % 500

rs200 = amount // 200
amount= amount % 200

rs100 = amount // 100
amount = amount % 100

rs50 = amount // 50
amount = amount % 50

rs20 = amount // 20
amount =amount % 20

rs10 = amount // 10
amount = amount % 10

min_notes =  rs500 + rs200 + rs100 + rs50 + rs20 + rs10 + amount

print(f'Minimum number of notes needed for representing the amount is : {min_notes}')