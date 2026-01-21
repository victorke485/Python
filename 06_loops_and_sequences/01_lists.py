# List is an ordered sequence of elements that can be comprised of strings, numbers or lists
# List data type are ordered and mutable

# Syntax:
cities = ["London", "Nairobi", "Tokyo", "Mombasa", "Nakuru", "Los Angeles"]

# Accessing elements:
print(cities[0])
print(cities[-1])

# list() constructor
language = "Python"
print(list(language))

# len() function
print(len(cities))

# Updating value
cities[0] = "Eldoret" 
print(cities)

# Removing element
del cities[0]
print(cities)

# Check an element if it is inside the list
print("Tokyo" in cities)

# Unpacking values from a list
developer = ["Victor", 20, "Python Developer"]
name, age, job = developer
print(f"Name: {name}\nAge: {age}\nJob: {job}")

# Slice Operator
print(cities)
print(cities[1:4])

numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1:4:2])


