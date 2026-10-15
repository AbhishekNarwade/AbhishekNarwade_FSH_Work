'''class Employee:
    def __init__(self, id1, name1, sal1):
        self.id = id1
        self.name = name1
        self.sal = sal1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getSal(self):
        return self.sal

    def setSal(self, newsal):
        self.sal = newsal

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tSal={self.sal}")

e1 = Employee(10, "Sachin", 121212)
e2 = Employee(18, "Virat", 33424)

print(e1.getName())
e1.display()
e2.display()
e2.setSal(8965)
e2.display()'''

# Example 1

'''class Car:
    def __init__(self, no1, name1, price1):
        self.no = no1
        self.name = name1
        self.price = price1

    def getNo(self):
        return self.no

    def setNo(self, newno):
        self.no = newno

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getPrice(self):
        return self.price

    def setPrice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"No={self.no}\tName={self.name}\tPrice={self.price}")


c1 = Car(101, "BMW", 7500000)
c2 = Car(102, "Audi", 6500000)

print(c1.getName())
c1.display()
c2.display()
c2.setPrice(7000000)
c2.display()'''

# Example 2

'''class Product:
    def __init__(self, id1, name1, price1):
        self.id = id1
        self.name = name1
        self.price = price1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getPrice(self):
        return self.price

    def setPrice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tPrice={self.price}")


p1 = Product(101, "Laptop", 55000)
p2 = Product(102, "Mobile", 25000)

print(p1.getName())
p1.display()
p2.display()
p2.setPrice(22000)
p2.display()'''

# Example 3

'''class Student:
    def __init__(self, roll1, name1, marks1):
        self.roll = roll1
        self.name = name1
        self.marks = marks1

    def getRoll(self):
        return self.roll

    def setRoll(self, newroll):
        self.roll = newroll

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getMarks(self):
        return self.marks

    def setMarks(self, newmarks):
        self.marks = newmarks

    def display(self):
        print(f"Roll={self.roll}\tName={self.name}\tMarks={self.marks}")


s1 = Student(101, "Rahul", 85)
s2 = Student(102, "Amit", 72)

print(s1.getName())
s1.display()
s2.display()
s2.setMarks(91)
s2.display()'''

# Example 4

'''class BankAccount:
    def __init__(self, accno1, name1, balance1):
        self.accno = accno1
        self.name = name1
        self.balance = balance1

    def getAccno(self):
        return self.accno

    def setAccno(self, newaccno):
        self.accno = newaccno

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getBalance(self):
        return self.balance

    def setBalance(self, newbalance):
        self.balance = newbalance

    def display(self):
        print(f"AccNo={self.accno}\tName={self.name}\tBalance={self.balance}")


b1 = BankAccount(1001, "Rohit", 50000)
b2 = BankAccount(1002, "Suresh", 35000)

print(b1.getName())
b1.display()
b2.display()
b2.setBalance(75000)
b2.display()'''

# Example 5

"""class Mobile:
    def __init__(self, id1, name1, price1):
        self.id = id1
        self.name = name1
        self.price = price1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getPrice(self):
        return self.price

    def setPrice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tPrice={self.price}")


m1 = Mobile(201, "OnePlus", 35000)
m2 = Mobile(202, "Samsung", 45000)

print(m1.getName())
m1.display()
m2.display()
m2.setPrice(42000)
m2.display()"""

# Dhyansetu
'''
class Student:
    def __init__(self, frn, name, bname, inmae):
        self.frn = frn
        self.name = name
        self.bname = bname
        self.inmae = inmae

    def getFrn(self):
        return self.frn 
    def setFrn(self, newfrn):
        self.frn = newfrn

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getBname(self):
        return self.bname
    def setBname(self, newbname):
        self.bname = newbname

    def getInmae(self):
        return self.inmae
    def setInmae(self, newinmae):
        self.inmae = newinmae

    def display(self):
        print(f"Frn={self.frn}\tName={self.name}\tBname={self.bname}\tInmae={self.inmae}")

s1 = Student(101, "Rahul", "17 api", "FBS")
s2 = Student(102, "Amit", "aug", "FBS") 
s3 = Student(103, "Rohit", "jul", "FBS")           
s1.display()
s2.display()
s3.display()'''

class Employee:
    def __init__(self, id1, name1, sal1):
        self.id = id1
        self.name = name1
        self.sal = sal1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getSal(self):
        return self.sal

    def setSal(self, newsal):
        self.sal = newsal

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tSal={self.sal}")

# Emp ends heae....

class Hr(Employee):
    def __init__(self, id1, name1, sal1, com1):
        super().__init__(id1, name1, sal1)
        self.com = com1

    def getCom(self):
        return self.com

    def setCom(self, newcom):
        self.com = newcom

    def display(self):
        print(f"Com={self.com}")
        return super().display()

# class Hr ends here....

class Developer(Employee):
    def __init__(self, id1, name1, sal1, bonus):
        super().__init__(id1, name1, sal1)
        self.bonus = bonus

    def getBonus(self):
        return self.bonus

    def setBonus(self, newbonus):
        self.bonus = newbonus

    def display(self):
        print(f"Bonus={self.bonus}")
        return super().display()    
# class Developer ends here....

e1 = Employee(10, "Sachin", 121212)
h1 = Hr(11, "Virat", 33424, "HR")
d1 = Developer(12, "Rohit", 8965, 5000)
e1.display()
h1.display()
d1.display()
