# Exception Handling
# try
try:
    print(x)
except:
    print("An exception occured")

# Many Exceptions
try:
    print(y)
except NameError:
    print("Variable y is not defined")
except:
    print("Something else went wrong")

# else - defines block of code if no errors were raised
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# finally - will be executed regardless if the bloc raises an error or not
try:
    print(z)
except:
    print("Something went wrong")
finally:
    print("Python is awesome")

# Raise an exception
w = -1
if w < 0:
    raise Exception("Sorry, no numbers below zero")