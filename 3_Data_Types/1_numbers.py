# int - whole number without decimals(positive or negative)
x = 1
print(type(x))

# float - number containing one or more decimals
y = 2.2
q = 34e4
print(q)
print(type(y))
print(type(q))

# complex - are written with j as the imaginary part
z = 2j
r = 4 + 9j
print(z)
print(type(z))
print(r)
print(type(r))


# Type Conversion
a = 4
b = 4.3
z = 4 + 5j

# int to float
a = float(a)
print(a)
print(type(a))

# float to int
b = int(b)
print(b)
print(type(b))

# int to complex
n = complex(b)
print(n)
print(type(n))

# You cannot convert any complex number into another number type
print(str(35.82))