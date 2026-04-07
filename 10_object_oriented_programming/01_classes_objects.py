# Class is like blueprint or template you use to create objects with.
# Object is what is created using that template
# Class: intializer, attributes and methods
# Attributes are like variables within a class and are used to store data
# Methods are functions defined within a class, and are the actions objects created with a class can perform

class ClassName:
    def __init__(self, name, age): # Special method automatically called when a new object is created
        self.name = name # Attributes the object will have
        self.age = age

    def sample_method(self): # Method each object created can call
        print(self.name.upper())

# When naming classes PascalCase is used
# self lets you access the object's own attributes and methods


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof!")

# Creating objects
dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

# Calling methods
dog_1.bark()
dog_2.bark()

print(dog_1.name)

# Attributes - are variables that belong to an object and they hold data
# Instance attributes - are unique to each object created from a class. Usually set with __init__ method
# Class attributes - belong to the class itself and are shared by all instances of that class

class Person:
    career = "Programmer" # Class attribute

    def __init__(self, name):
        self.name = name # Instance attribute

person_1 = Person("Alex")
print(person_1)
print(person_1.career)
print(person_1.name)

# Special methods / Magical methods / dunder methods - start and end with double underscores
print((3).__add__(4)) # 3+4

# eg: __add__(), __init__(), __len__(), __str__()

# Defining your own methods in memory
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"
    
    def __eq__(self, other):
       return self.pages == other.pages
    

book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1)) # 420
print(len(book2)) # 420
print(str(book1)) # 'Built Wealth Like a Boss' has 420 pages
print(str(book2)) # 'Be Your Own Start' has 420 pages
print(book1 == book2) # True


# Handling attributes dynamically
# getattr() - reads an attribute from an object, if the attribute doesn't exist, it raises an AttributeError unless you provide a default value
print(getattr(book1, "title"))
print(getattr(book1, "pages"))
print(getattr(book1, "rating", 4.6))

# dir() - returns a list of all attribute names on the object
print(dir(book1))

for attr in dir(book1):
    if not attr.startswith("__"):
        print(f"{attr}: {getattr(book1, attr)}")

# setattr() - lets you create a new attribute or update an existing one dynamically
setattr(book1, "category", "Business")
print(book1.category) 

# hasattr() - returns True or False
print(hasattr(book1, "category"))
print(hasattr(book1, "rating"))

# delattr() - lets you remove an attribute dynamically
delattr(book1, "category")
print(hasattr(book1, "category"))