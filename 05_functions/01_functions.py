# Functions are reusable pieces of code that run when you call them.
# Built in function : bool(), print(), input(), int()
def hello():
    name = input("Enter your name: ")
    print(f"Hello {name}")

hello()

# Functioin with parameters and arguments
def add(a, b):
    print(f"The addition of {a} and {b} is {a + b}")
add(12, 24)

"""
Parameter is the variable listed in the function defination
Argument is the actual value you pass to the function when called
In the above function:
    -a and  b are the parameters
    -12 and 24 are the arguments
"""

# Return keyword
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum)

# Positional and keyword argument
"""
Positional arguments are matched to parameters by their position in the function call eg calculate_sum() function above
Keyword argument are matched by the paramter name
"""

def mean(total_marks, no_of_students):
    return round((total_marks / no_of_students), 2)

print(mean(no_of_students=5, total_marks=100))

# Identifying keyword arguments
print(help(round))