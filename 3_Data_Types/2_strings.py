# Single line string
x = "Python"
print(x)
print(type(x))

# Multiline string
y = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(y)
print(type(y))

# String are arrays
print(x[0])

# Looping through a string
for i in "Python":
    print(i)

# String length
print(len(x))

# Check string - check if a certsin phrase or character is in a string
print("o" in x)
print("b" not in x)

# Slicing Strings
b = "Victor"
print(b[0:3])
print(b[-5:-2])

# Modifying Strings
v = "victor"
# Upper case
print(v.upper())
# Lower case
print(v.lower())
# Remove whitespace - space before or after the actual text
print(" Hello, world!   ".strip())
# Replace string
print(v.replace("v", "b"))
# Split string - splits the string into substrings if it finds instance of the separator
print("Python, is, awesome".split( "," ))


# String Conatenation
n1 = "Hello"
n2 = "World"
print(n1 + " " + n2)