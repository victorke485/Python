# Loop through a list
mylist = ["Javascript", "Python", "C", "Java"]
for i in mylist:
    print(i)

# Loop through the index numbers
for i in range(len(mylist)):
    print(mylist[i])

# Using a while loop
while i < len(mylist):
    print(mylist[i])
    i += 1

# Looping using list comprehension
[print(x) for x in mylist]

# List Comprehension - offers a shorter syntax when you want to create a new list based on the values of an existing list.
newlist = [x for x in mylist if "a" in x]
print(newlist)

# Sort lists
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)

# Reverse order
mylist = ["Javascript", "Python", "C", "Java"]
mylist.reverse()
print(mylist)

# Copy list
newlist = mylist.copy()
print(newlist)
newlist = list(mylist)
print(newlist)

# Join lists
# Using the + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# Appending all the items one by one
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)
# extend()
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
