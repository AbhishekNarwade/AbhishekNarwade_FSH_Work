# research on numeric valaur  in operand 
# ex: print(10 or '')
# o/p: 10  -----?
# r on logical operator with numeric value / string 


#1. and: If both the oprands are true then print true otherwise print false 

#   x          y           x & y
# false     false         false
# false     true          false
# true      false         false
# true      true          true

print(True and True)

#2. or:  If both the oprands are false then print false otherwise print true

#   x          y           x & y
# false     false         false
# false     true          true
# true      false         true
# true      true          true

print(False or False) 
print(True or False)

#3. not: opposite of oprands

print(not True)
print(not False)