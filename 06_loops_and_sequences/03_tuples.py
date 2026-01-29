# Tuples are immutable - elements in a tuple cannot be changed  once it is created

# Acessing an element in a tuple
my_tuple = ("Alex", "Amos", "Eliezer", "Abdi")
print(my_tuple[0])
print(my_tuple[-2])

# tuple() constructor
developer = "Victor"
print(tuple(developer))

# Checking if an item is in tuple
print("Amos" in my_tuple)

# Unpacking items from a list
person1, person2, person3, person4 = my_tuple
print(person1, person2, person3, person4)

name1, *other_names = my_tuple
print(f"First Name: {name1}\nOther Names: {other_names}")