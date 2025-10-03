# A class is like an object construcor or a 'blueprint' for creating objects

# Creating a class
class MyClass:
    x = 5
    
# Creating an object
p1 = MyClass()
print(p1.x)

# The __init__() Method - Always executed when the class is being initiates. Used to assign values to object properties
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = person("John", 23)

print(p2.name)
print(p2.age)

# The __str__() Method - controls what should be returned when the class object is represented as a string
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} {self.age}"

p1 = Person("John", 36)

print(p1)

# Create Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# the self Parameter - is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like,
# but it has to be the first parameter of any function in the class:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties
p1.age = 40

# Delete Object Properties
del p1.age

# Delete Objects
del p1

# The pass statement - used for class with no content
class Person:
  pass