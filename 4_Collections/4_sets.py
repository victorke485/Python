# Are used to sore multiple values in a single variable
"""
-Unordered
-Unchangeable
-Unindexed
-Duplicates are not allowed
"""

myset = {"Python", "Java", "Javascript", "Ruby"}
print(myset)
print(type(myset))

# Get length
print(len(myset))

# The set() Constructor
thisset = set(("Ubuntu", "Mint", "Arch", "Fedora", "Pop", ))
print(type(thisset))

# Check if item is in set
print("Python" in myset)
print("Python" not in myset)

# Add new items
myset.add("R")

# Add sets
myset.update(thisset)
print(myset)

# Remove set items
myset.remove("Pop")
myset.discard("R")

# Remove random item
myset.pop()

# Empty the set
myset.clear()

# Delete set
del myset