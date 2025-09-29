# Use to store multiple items in a single variable
"""
-Are ordered
-Are unchangble
-Allow duplicate values
"""
mytuple = ("Python", "Java", "Javascript", "SQL", "C", "C++")
print(mytuple)
print(type(mytuple))

# Tuple length
print(len(mytuple))

# Creating tuple with one item - , after the item
thistuple = ("apple",)
print(type(thistuple))

# The tuple() constructer
tuple1 = tuple(("Ubuntu", "Arch", "Mint", "Fedora"))

# Accesing items in tuple
print(mytuple[0])

# Check if item exists
print("Python" in mytuple)

# Changing tuple values
mylist1 = list(mytuple)
mylist1[0] = "Rust"
mytuple = tuple(mylist1)
print(mytuple)

# Adding tuple to a tuple
newtuple = tuple1 + mytuple + ("Go",)
print(newtuple)

# Deleting tuple: del mytuple

# Unpacking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# Tuple methods
# count()- Returns the number of times a specified value occurs in a tuple
print(fruits.count("apple"))

# index()- Searches the tuple for a specified value and returns the position of where it was found
print(fruits.index("apple"))