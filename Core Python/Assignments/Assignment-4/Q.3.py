# 3. WAP to print the sum of all numbers until n.

num = int(input("Enter a number: "))
i = 0
sum = 0
for i in range(1, num + 1):
    sum += i
print(f"The sum of all numbers until {num} is: {sum}")
