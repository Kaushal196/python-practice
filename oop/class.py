class Employee:
    def __init__(self, fname, lname, age):
        #instance var unique for each instance
        self.fname = fname
        self.lname = lname
        self.email = self.fname + '.' + self.lname + '@company.com'
        self.age = age 

    def fullName(self):
        return f'{self.fname} {self.lname}'         

emp1 = Employee('Kaushal','Pandey', 25)
emp2 = Employee('Test','User', 30)

#emp1 and and emp2 are two diff instance of Employee class
print(emp1.email)
print(emp2.age)

print(emp1.fullName())
print(Employee.fullName(emp1)) #if we use this way we need to pass instance 