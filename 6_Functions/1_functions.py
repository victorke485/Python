# Creating a function
def my_function():
    print("Hello from a function")


# Calling a function
my_function()


# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# Arbitrary Keyword Arguments, **kwargs - used when you do not know how many keyword arguments that will be passed into your function
def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Victor", lname="Mutua")


# Default parameter value
def function1(country="Kenya"):
    print(f"I am from {country}")


function1()


# Passing list as an Argument
def my_languages(languages):
    for x in languages:
        print(x)


p_languages = ["Python", "Java", "GO"]
my_languages(p_languages)


# Return a value
def my_function(x):
    return 5 * x


# The pass statement- used when a function has no content
def myfunction():
    pass


# Recursion - function calling itself
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(6)
