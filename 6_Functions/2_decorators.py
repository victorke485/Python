# Lets you add extra behavior to a function
# Is a function that takes another function as input and returns a new function


# Basic Decorator
def changecase(func):
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Hello Sally"


print(myfunction())


# Argument in the decorated function
def changecase(func):
    def myinner(x):
        return func(x).upper()

    return myinner


@changecase
def myfunction(nam):
    return "Hello " + nam


print(myfunction("John"))

# Preserving Function Metadata
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)