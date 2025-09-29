# Joining sets
set1 = {"Python", "C", "Java", "Ruby", "Golang"}
set2 = {"Ubuntu", "Fedora", "Debian", "Parrot"}

# Union - returns a new set with all items from both sets
set3 = set1.union(set2)
print(set3)
set4 = set1 | set2
print(set4)

# Join a set and a tuple
x = {1, 2, 3, 4}
y = ("a", "b", "c")
z = x.union(y)
print(z)

# Update - inserts all items from one set into another.
set1.update(set2)
print(set1)

# Intersection - return a new set, that only contains the items that are present in both sets.
seta = {"apple", "banana", "cherry"}
setb = {"google", "microsoft", "apple"}

setc = seta.intersection(setb)
print(setc)

setx = seta & setb
print(setx)

# intersection_update - keep only the duplicates, but it will change the original set instead of returning a new set
seta.intersection_update(setb)
print(seta)
print("--------------------------")

# Difference - will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

set4 = set2 - set1
print(set4)

# diffrence_update() - keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1.difference_update(set2)
print(set1)

print("------------Symmetric Difference-----------")

# Symmetric Diffeences - he symmetric_difference() method will keep only the elements that are NOT present in both sets.
setm = {"Arsenal", "Chelsea", "Liverpool"}
setn = {"Madrid", "Burnley", "Man city", "Arsenal"}
setp= setm.symmetric_difference(setn)
print(setp)

setr= setm ^ setn
print(setr)

# symmetric_difference_update() - keep all but the duplicates, but it will change the original set instead of returning a new set
setm.symmetric_difference_update(setn)
print(setm)