# Single line string
my_str_1 = "Hello"
print(my_str_1)

# Multi line string
my_str_2 = """Multiline
string
"""
print(my_str_2)

# If string contains either single or double quatation marks
print("It's a sunny day")
print("She said, \"Hello World!\"")

# To check if a string contains one or more charactes
my_str = "Hello world"
print("Hello" in my_str)
print("hell" in my_str)
print("python" in my_str)
print(" " in my_str)

# Length of a string
print(len("hello world"))

# Index of character in a string
language = "Python"
print(language[0])
print(language[-1])

# String concatenation
print("Hello" + " " + "World" + "!") 

# To cancatenate a string and a number
age = 12
name = "John"
print(name + str(age))

# String interpolation - process of inserting variables and expessions into a string
# f-strings - formatted string literals
print(f"His name is {name} and he is {age} years old")

num1 = 12
num2 = 90
print(f"The sum of {num1} and {num2} is {num1 + num2}")

# String slicing - string[start:stop:step]
name = "Alexandar"
print(name[0:4])
print(name[:4])
print(name[4:])
print(name[0:9:2])

print(name[::-1]) # Reverses string

# String methods
my_new_string = "   You TUbe    "

print( my_new_string.upper() )
print( my_new_string.lower() )
print( my_new_string.strip() ) # Returns a new string with the specified leading and trailing characters removed
print( my_new_string.replace("You", "My") ) # replace(old, new) - Returns a new string with all occurences of old replaced by new
print( my_new_string.split() )  # split(separator): Splits a string on a specified separator into a list of strings. If no separator is specified, it splits on whitespace.

# join(iterable): Joins elements of an iterable into a string with a separator
my_list = ["hello", "world"]

joined_my_str = " ".join(my_list)
print(joined_my_str)

# startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix
my_str = "hello world"
print(my_str.startswith("hello"))

# endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix
my_str = "hello world"
print( my_str.endswith("world") )

# find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one.
my_str = "hello world"

world_index = my_str.find("world")
print(world_index)

# count(substring): Returns the number of times a substring appears in a string.
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)

# capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.
my_str = "hello wORLd"

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)

# isupper(): Returns True if all letters in the string are uppercase and False if not.
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)

# islower(): Returns True if all letters in the string are lowercase and False if not.
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)

# title(): Returns a new string with the first letter of each word capitalized.
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)