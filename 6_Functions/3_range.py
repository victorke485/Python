# range() returns an immutable sequence of numbers
# range(start, stop, step)

x = range(10)
print(x)
print(type(x))
print(list(range(10)))
print(list(range(5, 10, 3)))

# Slicing Ranges
r = range(5, 10)
print(r[2])
print(r[:3])

# Membership Testing
z = range(10)
print(8 in r)
print(12 in r)

# Length
print(len(range(10)))