'''
# Abstraction

from abc import ABC,abstractmethod
class Student(ABC):
    def __init__(self, id1, name1, fees1):
        self.id = id1
        self.name = name1
        self.fees = fees1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getFees(self):
        return self.fees

    def setFees(self, newfees):
        self.fees = newfees

    @abstractmethod
    def calsal(self):
        pass

    def __str__(self):
        return f"Id={self.id}\tName={self.name}\tFees={self.fees}"

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tFees={self.fees}")


class EngineeringStudent(Student):
    def __init__(self, id1, name1, fees1, labfees):
        super().__init__(id1, name1, fees1)
        self.labfees = labfees

    def calsal(self):
        print(f"Final fees of Engineering={self.fees + self.labfees}")

    def __str__(self):
        return super().__str__() + f"\tLab Fees={self.labfees}"
    
    def display(self):
        print(f"Lab Fees={self.labfees}")
        super().display()


class MedicalStudent(Student):
    def __init__(self, id1, name1, fees1, practicalfees):
        super().__init__(id1, name1, fees1)
        self.practicalfees = practicalfees

    def calsal(self):
        print(f"Final fees of Medical={self.fees + self.practicalfees}")

    def __str__(self):
        return super().__str__() + f"\tPractical Fees={self.practicalfees}"
    
    def display(self):
        print(f"Practical Fees={self.practicalfees}")
        super().display()
#s1 = Student(10, "Amit", 20000)
e1 = EngineeringStudent(11, "Rahul", 60000, 5000)
m1 = MedicalStudent(12, "Priya", 80000, 10000)

#print(s1)
print(e1)
print(m1)
'''


'''
# Encapsulation

class Product:
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
p2.display()
'''

'''
# Inheritance

class Product:
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
l1.display()
'''

'''
# Polymorphism

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
'''

'''
# __str__ method example

class Student:
    def __init__(self, id1, name1, fees1):
        self.id = id1
        self.name = name1
        self.fees = fees1

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getFees(self):
        return self.fees

    def setFees(self, newfees):
        self.fees = newfees


    def calsal(self):
        print(f"Final fees of Student={self.fees}")

    def __str__(self):
        return f"Id={self.id}\tName={self.name}\tFees={self.fees}"

    def display(self):
        print(f"Id={self.id}\tName={self.name}\tFees={self.fees}")


class EngineeringStudent(Student):
    def __init__(self, id1, name1, fees1, labfees):
        super().__init__(id1, name1, fees1)
        self.labfees = labfees

    def calsal(self):
        print(f"Final fees of Engineering={self.fees + self.labfees}")

    def __str__(self):
        return super().__str__() + f"\tLab Fees={self.labfees}"
    
    def display(self):
        print(f"Lab Fees={self.labfees}")
        super().display()


class MedicalStudent(Student):
    def __init__(self, id1, name1, fees1, practicalfees):
        super().__init__(id1, name1, fees1)
        self.practicalfees = practicalfees

    def calsal(self):
        print(f"Final fees of Medical={self.fees + self.practicalfees}")

    def __str__(self):
        return super().__str__() + f"\tPractical Fees={self.practicalfees}"
    
    def display(self):
        print(f"Practical Fees={self.practicalfees}")
        super().display()
s1 = Student(10, "Amit", 20000)
e1 = EngineeringStudent(11, "Rahul", 60000, 5000)
m1 = MedicalStudent(12, "Priya", 80000, 10000)

print(s1)
print(e1)
print(m1)
'''