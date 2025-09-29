a = 232
b = 43

if a > b:
    print("a is greater than b")
    
if a > b : print("a is greater than b")

# Elif
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

print("A") if a > b else print("B")