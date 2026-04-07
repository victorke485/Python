# OOP is a programming style in which developers treat everything in their code like a real-world object
# OOP has 4 key principles: encapsulation, inheritance, polymorphism and abstraction

# Encapsulation is the bundling of the attributes and methods of an object into a single unit, the class

# By prefixing attributes and methods with a single underscore means they are meant for intenal use
# double underscore effectively prevents them to be accessed from the outside of their class, making those attributes and methods private


class Wallet:
    def __init__(self):
        self.__balance = 0 # Private attribute

    def __validate(self, amount): # Private method
        if amount < 0:
            raise ValueError("Amount must be positive")

    def deposit(self, amount):
        self.__validate(amount)
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
my_wallet = Wallet()
my_wallet.deposit(120)
print(my_wallet.get_balance())

# Getters and Setters - are methods that let you control how the attributes of a class are accessed and modified
# getters - retrieve a value
# setters - you set a value
# Done through properties - act like attributes but behave like methods under the hood
# Make your code cleaner and easy to read

# A deleter control how an attribute is deleted

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Getter
    @property
    def radius(self):
        return self._radius

    # Setter
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # Deleter
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius

# Create circle object with a radius
my_circle = Circle(33)
print("Initial radius:", my_circle.radius)  # 33

# Delete the radius
# This calls the deleter
del my_circle.radius # Deleting radius...
print("Radius deleted!") # Radius deleted!

# Try to access radius after deletion
try:
    print(my_circle.radius)
except AttributeError as e:
    print("Error:", e) # Error: 'Circle' object has no attribute '_radius'


# Getters let you retrieve a value or even compute a value on the fly.
# Setters let you modify the values safely by running checks before assignment.
# Properties are what tie these getters and setters together so you can write logic while still using dot notation.
# Deleters let you define what happens when an attribute is deleted.