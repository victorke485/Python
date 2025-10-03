# Inheritance allows us to define a class that can inherit all the methods and properties from other class
# Parent class/ base class - class  being inherited from
# Child class/ derived class - class that inherits from another class

# Crate a parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

# Create a child class
class Student(Person):
    pass

x = Student("Mike", "Mutua")
x.printname()

# the super() function - makes the child class inherit all the methods and properties from its parent
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        
        # Add properties:
        self.graduationyear = year

x = Student("mike", "Olsen", 2025)
x.printname()
print(f"{x.graduationyear}")