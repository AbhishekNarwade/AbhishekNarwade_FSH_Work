# 5. WAP to calculate selling price of book based on cost price and discount.

cost = float(input('enter the coset : '))
discount = float(input('enter the discount : '))
selling_price = cost - (cost * discount / 100)
print(f'the selling price of book based on {cost} cost price and {discount} discount is : {selling_price}')