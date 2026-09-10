# 5. A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST

product1 = int(input('ENter the price : '))
product2 = int(input('ENter the price : '))
product3 = int(input('ENter the price : '))
product4 = int(input('ENter the price : '))
product5 = int(input('ENter the price : '))

total_prize = product1 + product2 + product3 + product4 + product5

gst = (total_prize * 18) / 100
total_bill = total_prize + gst
print(total_bill)