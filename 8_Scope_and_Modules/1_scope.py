# Local scope - A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def myfunc():
    x = 9
    print(x)

myfunc()

# Functions inside a function
# Variable is not available outside a function but is avialable for any function inside the function
def myfunction1():
    q = "Python"
    def myfunction2():
        print(q)
    myfunction2()

myfunction1()

# Global keyword - used to create global variable inside a function
def myfunc1():
    global y
    y = 788

myfunc1()

print(y)

# Also used to change a global variable inside a function
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

# Nonlocal Keyword - used to work with variables inside nested functions.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())