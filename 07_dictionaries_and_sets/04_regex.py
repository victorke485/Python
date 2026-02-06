import re

# A regular expression, or regex, is a pattern used to match a sequence of characters in text

# search function
greeting = "Hello there!"
print(re.search("Hi", greeting))
print(re.search("hello", greeting))
print(re.search("hello", greeting, re.IGNORECASE))

# To check if a string has numbers
id = "P12"
print(re.search("\d", id))

print("-"*100)

# fullmatch function returns a match object when the regex pattern matches the entire string and None otherwise

book = "Fahrenheit 451"
print(re.fullmatch("\d+", book))

print(re.fullmatch("Fahrenheit \d+", book))

print("-" * 100)
x = [1, 3]
print(all(x))