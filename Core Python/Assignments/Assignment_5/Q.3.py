'''' 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
passenger and then calculate total amount to ticket to travel for all of them based on
following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.'''

passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter per ticket cost: "))
total_amount = 0

for i in range(1, passengers + 1):
    age = int(input(f"Enter age of passenger {i}: "))
    
    if age < 12:
        discount = 0.30 * ticket_cost
    elif age > 59:
        discount = 0.50 * ticket_cost
    else:
        discount = 0
    
    final_cost = ticket_cost - discount
    total_amount += final_cost

print(f"Total amount for all passengers: {total_amount}")