# Lists are used to store multiple items in a single variable
"""
- Are ordered
- Are changeable
- Allow duplicate values
- Can be of any data types
- Can contain different data types
"""
mylist = ["python", "html", "css", "javascipt"]
print(mylist)

# List length
print(len(mylist))

# type()
print(type(mylist))

# The list() constructer
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# Access list items
print(mylist[1])
print(mylist[-1])
print(mylist[1:3])
print(mylist[-4:-1])

# Check if item exist
print("python" in mylist)

# Change list items
mylist[0] = "C"
print(mylist)

# Change a range of item values
mylist[1:3] = ["C++", "Rust"]
print(mylist)

# Insert Items
mylist.insert(0, "Python")
print(mylist)


# Add list items
mylist.append("Rust")
print(mylist)

# Extend List
list1 = ["Ubuntu", "Arch", "Fedora", "Debian"]
mylist.extend(list1)
print(mylist)

# Remove list items
mylist.remove("Debian")
print(mylist)

# Remove Specified index
mylist.pop(0)
print(mylist)

# If not you do not specify the index, the pop() method removes the last item.
mylist.pop()
print(mylist)

# The del() keyword deletes the list completely
# del mylist
# print(mylist)

# Clear the list
mylist.clear()
print(mylist)