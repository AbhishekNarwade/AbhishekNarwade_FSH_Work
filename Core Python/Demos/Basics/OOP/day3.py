'''class Student:
    inName = "FBS"
    @staticmethod
    def setInName(newinname):
        Student.inName = newinname

    def __init__(self, frn, name, bname):
        self.frn = frn
        self.name = name
        self.bname = bname

    def display(self):
        print(f"Frn={self.frn}\tName={self.name}\tBname={self.bname}\tInmae={Student.inName}")    

#s1 = Student(201, "Dhyansetu", "FBS")
#s2 = Student(202, "Rahul", "FBS")          
#Student.setInName("FBS-2024")
#s1.display()
#s2.display()
print(Student.inName)
Student.setInName("Firstbit Solutions")
print(Student.inName)'''

'''class Student:
    stCount = 0
    
    def __init__(self, frn, name, bname):
        self.frn = frn
        self.name = name
        self.bname = bname
        Student.stCount += 1

    def display(self):
        print(f"Frn={self.frn}\tName={self.name}\tBname={self.bname}\tInmae={Student.inName}")    

class placedStudent(Student):
    def __init__(self, frn, name, bname, cname):
        self.frn = frn
        self.name = name
        self.bname = bname
        self.cname = cname

    def display(self):
        print(f"Frn={self.frn}\tName={self.name}\tBname={self.bname}\tCname={self.cname}")
        
s1 = Student(201, "Abhishek", "April")
s2 = Student(202, "Rahul", "May")
s3 = Student(203, "Rohit", "June")
s4 = placedStudent(204, "Amit", "July", "TCS")
s5 = placedStudent(205, "Ramesh", "August", "Infosys")
print(Student.stCount)'''

# INHERANCE

'''class Student:
    stCount = 0
    
    def __init__(self, frn, name, bname):
        self.frn = frn
        self.name = name
        self.bname = bname
        Student.stCount += 1

    def display(self):
        print(f"Frn={self.frn}\tName={self.name}\tBname={self.bname}\tInmae={Student.inName}")    

class placedStudent(Student):
    def __init__(self, frn, name, bname, Cname):
        super().__init__(frn, name, bname)
        self.cName= self.cName
    def setCname(self.cName):
        self.cName= cName 
    def getCName    

    
        
s1 = Student(201, "Abhishek", "April")
s2 = Student(202, "Rahul", "May")
s3 = Student(203, "Rohit", "June")
s4 = placedStudent(204, "Amit", "July", "TCS")
s5 = placedStudent(205, "Ramesh", "August", "Infosys")
print(Student.stCount)'''

# Example 1

'''class Animal:
    def __init__(self, id1, name1, age1):
        self.id = id1
        self.name = name1
        self.age = age1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getAge(self):
        return self.age

    def setAge(self, newage):
        self.age = newage

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tAge={self.age}")


# Animal ends here....


class Dog(Animal):
    def __init__(self, id1, name1, age1, breed):
        super().__init__(id1, name1, age1)
        self.breed = breed

    def getBreed(self):
        return self.breed

    def setBreed(self, newbreed):
        self.breed = newbreed

    def display(self):
        print(f"Breed={self.breed}")
        return super().display()


# class Dog ends here....


class Cat(Animal):
    def __init__(self, id1, name1, age1, color):
        super().__init__(id1, name1, age1)
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, newcolor):
        self.color = newcolor

    def display(self):
        print(f"Color={self.color}")
        return super().display()


# class Cat ends here....


a1 = Animal(10, "Tiger", 5)
d1 = Dog(11, "Tommy", 3, "Labrador")
c1 = Cat(12, "Kitty", 2, "White")

a1.display()
d1.display()
c1.display()'''

# Example 2

'''class Vehicle:
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


# Vehicle ends here....


class Car(Vehicle):
    def __init__(self, id1, name1, price1, model):
        super().__init__(id1, name1, price1)
        self.model = model

    def getModel(self):
        return self.model

    def setModel(self, newmodel):
        self.model = newmodel

    def display(self):
        print(f"Model={self.model}")
        return super().display()


# class Car ends here....


class Bike(Vehicle):
    def __init__(self, id1, name1, price1, cc):
        super().__init__(id1, name1, price1)
        self.cc = cc

    def getCc(self):
        return self.cc

    def setCc(self, newcc):
        self.cc = newcc

    def display(self):
        print(f"CC={self.cc}")
        return super().display()


# class Bike ends here....


v1 = Vehicle(10, "Vehicle", 50000)
c1 = Car(11, "Swift", 700000, "VXI")
b1 = Bike(12, "Pulsar", 120000, 150)

v1.display()
c1.display()
b1.display()'''

# Example 3

'''class BankAccount:
    def __init__(self, id1, name1, balance1):
        self.id = id1
        self.name = name1
        self.balance = balance1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getBalance(self):
        return self.balance

    def setBalance(self, newbalance):
        self.balance = newbalance

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tBalance={self.balance}")


# BankAccount ends here....


class SavingsAccount(BankAccount):
    def __init__(self, id1, name1, balance1, interest):
        super().__init__(id1, name1, balance1)
        self.interest = interest

    def getInterest(self):
        return self.interest

    def setInterest(self, newinterest):
        self.interest = newinterest

    def display(self):
        print(f"Interest={self.interest}")
        return super().display()


# class SavingsAccount ends here....


class CurrentAccount(BankAccount):
    def __init__(self, id1, name1, balance1, overdraft):
        super().__init__(id1, name1, balance1)
        self.overdraft = overdraft

    def getOverdraft(self):
        return self.overdraft

    def setOverdraft(self, newoverdraft):
        self.overdraft = newoverdraft

    def display(self):
        print(f"Overdraft={self.overdraft}")
        return super().display()


# class CurrentAccount ends here....


b1 = BankAccount(10, "Sachin", 50000)
s1 = SavingsAccount(11, "Virat", 80000, 7)
c1 = CurrentAccount(12, "Rohit", 100000, 50000)

b1.display()
s1.display()
c1.display()'''

# Example 4

'''class Student:
    def __init__(self, id1, name1, marks1):
        self.id = id1
        self.name = name1
        self.marks = marks1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getMarks(self):
        return self.marks

    def setMarks(self, newmarks):
        self.marks = newmarks

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tMarks={self.marks}")


# Student ends here....


class EngineeringStudent(Student):
    def __init__(self, id1, name1, marks1, branch):
        super().__init__(id1, name1, marks1)
        self.branch = branch

    def getBranch(self):
        return self.branch

    def setBranch(self, newbranch):
        self.branch = newbranch

    def display(self):
        print(f"Branch={self.branch}")
        return super().display()


# class EngineeringStudent ends here....


class MedicalStudent(Student):
    def __init__(self, id1, name1, marks1, specialization):
        super().__init__(id1, name1, marks1)
        self.specialization = specialization

    def getSpecialization(self):
        return self.specialization

    def setSpecialization(self, newspecialization):
        self.specialization = newspecialization

    def display(self):
        print(f"Specialization={self.specialization}")
        return super().display()


# class MedicalStudent ends here....


s1 = Student(10, "Amit", 75)
e1 = EngineeringStudent(11, "Rahul", 85, "Computer")
m1 = MedicalStudent(12, "Priya", 90, "Cardiology")

s1.display()
e1.display()
m1.display()'''


# Example 5

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


# Product ends here....


class Mobile(Product):
    def __init__(self, id1, name1, price1, camera):
        super().__init__(id1, name1, price1)
        self.camera = camera

    def getCamera(self):
        return self.camera

    def setCamera(self, newcamera):
        self.camera = newcamera

    def display(self):
        print(f"Camera={self.camera}")
        return super().display()


# class Mobile ends here....


class Laptop(Product):
    def __init__(self, id1, name1, price1, ram):
        super().__init__(id1, name1, price1)
        self.ram = ram

    def getRam(self):
        return self.ram

    def setRam(self, newram):
        self.ram = newram

    def display(self):
        print(f"RAM={self.ram}")
        return super().display()


# class Laptop ends here....


p1 = Product(10, "Product", 10000)
m1 = Mobile(11, "OnePlus", 30000, "50MP")
l1 = Laptop(12, "HP", 60000, "16GB")

p1.display()
m1.display()
l1.display()'''


class Product:
    def __init__(self, id1, name1, price1, ):
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

    def calsal(self):
        return self.price + 1000    

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tPrice={self.price}")


# Product ends here....


class Mobile(Product):
    def __init__(self, id1, name1, price1, camera):
        super().__init__(id1, name1, price1)
        self.camera = camera

    def getCamera(self):
        return self.camera

    def setCamera(self, newcamera):
        self.camera = newcamera

    def calsal(self):
        print(f"final salary of hr {self.price + self.camera}")    

        

    def display(self):
        print(f"Camera={self.camera}")
        return super().display()


# class Mobile ends here....


class Laptop(Product):
    def __init__(self, id1, name1, price1, ram):
        super().__init__(id1, name1, price1)
        self.ram = ram

    def getRam(self):
        return self.ram

    def setRam(self, newram):
        self.ram = newram

    
    def calsal(self):
        print(f"final salary of laptop {self.price + self.ram}") 

    def display(self):
        print(f"RAM={self.ram}")
        return super().display()


# class Laptop ends here....


p1 = Product(10, "Product", 10000)
m1 = Mobile(11, "OnePlus", 30000, 4444)
l1 = Laptop(12, "HP", 60000, 443)

p1.calsal()
m1.calsal()
l1.calsal()