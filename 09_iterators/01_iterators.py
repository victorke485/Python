# Iterable - object with an associated iter() method
# Iterator - produces next value with next()

# Creating iterator from an iterable
name = "Victor"
it = iter(name)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

name = "Victor"
it = iter(name)
print(*it)


# Iterating over dict
person = {
    "name": "Victor",
    "age": 19,
    "hobby": "coding",
}
for key, value in person.items():
    print(key, value)


# Iterating over file connections
file = open("./09_iterators/file.txt")
it = iter(file)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# enumerate() - returns an iterator of tuples containing indices and values
names = ["James", "Alex", "Kim"]
e = enumerate(names)
print(list(e))

b = enumerate(names, start=10)
for key, value in b:
    print(key, value)

# Zip
languages = ["Python", "Java", "Javascript"]
z = zip(names, languages)
for z1, z2 in z:
    print(z1, z2)

