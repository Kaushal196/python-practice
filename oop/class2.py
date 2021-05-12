class Employee:
    # class var
    no_of_employee = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = f'{fname}.{lname}@gmail.com'
        Employee.no_of_employee += 1
    
    #regular methods in a class automatically takes self as arg
    def fullName(self):
        return f'{self.fname} {self.lname}'
    
    def applyraise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('k', 'p', 50000)
emp2 = Employee('test', 'one', 60000)

Employee.raise_amount = 1.05
# if we change class var like this it will change its value for all instances
print(emp1.raise_amount) #1.05
print(emp2.raise_amount) #1.05

#It will create a new instnce var for emp1 will not affect others
emp1.raise_amount = 2.0
print(emp1.raise_amount) #2.0
print(emp2.raise_amount) #1.05   
print(Employee.raise_amount) #1.05
