class Employee:
    def __init__(self):
        print("Employee Constructor")
    def display(self):
        print("Employee Display")
e1 = Employee()
e2 = Employee()
print(f'id of e1 = {id(e1)}')
print(f'id of e2 = {id(e2)}')