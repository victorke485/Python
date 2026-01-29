programming_languages = ("Python", "Java", "C", "C++", "Rust", "C#", "Python")

# count() - used to determine how many times an item appears in a tuple
print(programming_languages.count("Python"))

# index() - used to find the index where a particular item is present in a tuple
print(programming_languages.index("Python"))

# You can also specify the starting searchung index and stopping index
print(programming_languages.index("Python", 3, 7))

# Sorting tuples
print(sorted(programming_languages, reverse=True))
print(sorted(programming_languages, key=len))