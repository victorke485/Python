# Are used to store data values in key
"""
-Ordered
-Changeable
-Do not allow duplicates
"""
mydict= {
    "name": "Victor",
    "age": 19
}
print(mydict)
print(type(mydict))

# Dictionary length
print(len(mydict))

# The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")

# Accessing items
print(mydict["name"])
print(mydict.get("age"))

# keys()- returns a list of all the keys in the dictionary.
print(mydict.keys())

# values() - returns a list of values
print(mydict.values())

# items() - returns each item in a dictionary as tuple in a list
print(mydict.items())

# Check if a key exists
print("name" in mydict)

# Change values
mydict["age"] = 20
mydict.update({"name": "Vicky"})
print(mydict)

# Adding Items
mydict["Proffesion"] = "Student"
mydict.update({"hobby": "coding"})
print(mydict)

# Removing items
mydict.pop("Proffesion")
mydict.popitem()
del mydict["age"]
print(mydict)

# Copying dictionaries
newdict = mydict.copy()
newdict = dict(mydict)

# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}