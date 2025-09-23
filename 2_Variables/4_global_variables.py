# Global variables - variables created outside of a function
x = "Python"

# Local variables - variables created inside a function
def myfunc():
    y = "awesome"

# The global keyword - used to create a global variable inside a function
def myfunction():
    global z
    z = "is"

myfunction()
print(x , z, "awesome")