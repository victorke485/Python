# A data type describes the kind of value a variable holds
# Python is dynamically-typed language meaning you do not need to explicitly declare types for variables

# Integer - a whole number without decimals
x = 12
print(x, "is of type:", type(x))

x = 12_232_234
print(x, "is of type:", type(x))

# Float - a number with a decimal point
a = 34.13
print(a, "is of type:", type(a))

# String - a sequence of characters enclosed in single or double quotation marks
my_string = "Hello World!"
print(my_string, "is of type:", type(my_string))

# Boolean - a true or false type, written as True or False.
is_awake = True
print(is_awake, "is of type:", type(is_awake))

# Set - an unordered collection of unique elements
my_set = {2, 3, 4}
print(my_set, "is of type:", type(my_set))

# Dictionary - a colection of key-value pairs encloded in curly braces
my_dict = {
    "name": "victor",
    "age": 12
}
print(my_dict, "is of type:", type(my_dict))

# Tuple - an immutable ordered collection
my_tuple = (12, 23, 23)
print(my_tuple, "is of type:", type(my_tuple))

# Range - a sequance of numebers, often used in loops
my_range = range(5)
print(my_range, "is of type:", type(my_range))

# List -an ordered collection of elements that supports different data types
my_list = [22, "Python", True]
print(my_list, "is of type:", type(my_list))

# None - a special value that represents the absence of a value
my_none_var = None
print(my_none_var, "is of type:", type(my_none_var))

# isinstance() function lets you check if a variable matches a specific data type
print( isinstance(12, int) )
print( isinstance(1.2, int) )
print( isinstance(True, bool) )
