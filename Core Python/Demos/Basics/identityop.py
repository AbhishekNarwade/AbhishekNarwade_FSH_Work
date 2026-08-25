x = 10   # immutable 
y = 10
z = 20
li1 = [10, 20]   # mutable
li2 = [10, 20]

#1. is

print(x is y)
print(li1 is li2)
print(id(x))
print(id(y))
print(id(li1))
print(id(li2))

#2. is not

print(x is not y)
print(li1 is not li2)
