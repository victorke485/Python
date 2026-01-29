# append() - add an item to the end of list
languages = ["Python", "Java", "Rust", "C", "Golang"]
languages.append("Javascript")
print(languages)

# extend() - add multiple elements from one list to another
numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7, 9]
numbers.extend(odd_numbers)
print(numbers)

# insert() - inserts an element at a specific index
languages.insert(0, "C++")
print(languages)

# remove() removes the element specified from a list
languages.remove("Golang")
print(languages)

# pop()-removes element at a specific index. If not specified the last element is removed
languages.pop(4)
print(languages)

# sort() - sort elements in place
languages.sort()
print(languages)

# sorted() - function which works for any iterable and returns a new sorted list instead of modifying the original list.
cars = ["BMW", "Audi", "Benz"]
sorted_cars = sorted(cars)
print(sorted_cars)

# Reverse - reverses a list of elements
languages.reverse()
print(languages)

# index() - finds the first index where an element can be found in a list
print(languages.index("Python"))

# clear() - empties a list
languages.clear()
print(languages)



