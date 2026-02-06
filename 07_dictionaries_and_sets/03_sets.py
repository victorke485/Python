# sets - don't store duplicate values, mutable(can be changed) and unordered
# Syntax:
my_set = {1, 2, 3, 4, 5}
print(type(my_set))
print(my_set)

# Declaring am empty set
new_set = set()

# Adding an element
my_set.add(6)
print(my_set)

# Removing an element from a set
# .remove() - raises a KeyError if the element is not found
my_set.remove(1)
print(my_set)
my_set.discard(6)
print(my_set)

# Remove all elements
my_set.clear()
print(my_set)

# .issubset() and .issuperset() methods checks  if a set is a subset or superset of another set respectively
set_1 = {1, 2, 3, 4, 5}
set_2 = {2, 3, 4, 5, 8, 9}

print(set_2.issubset(set_1))
print(set_2.issuperset(set_1))

# More explanation: A set A is a subset of B if every element of A exists in B
# A set B is a superser of A if it contains all elements of A

# .isdisjoint() - checks if 2 sets dont have anylement i common
print(set_1.isdisjoint(set_2))

# | --> returns a new set with all elements from both sets
print(set_1 | set_2)

# & --> returns a new set with only the elements that the sets have in common
print(set_1 & set_2)

# - --> retuns a new set with the elements of the first set that are not in the other sets
print(set_1 - set_2)

# ^ --> returns a new set with the elements that are either in the first or the second set, but not both
print(set_1 ^ set_2)

# if you add = sign after each above operators, the results are assigned to the first set
set_1 ^= set_2
print(set_1)

# Check if an element is in a ser
print(9 in set_1)