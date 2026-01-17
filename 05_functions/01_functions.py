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


# Return keyword
def calculate_sum(a, b):
    return a + b


my_sum = calculate_sum(3, 1)
print(my_sum)
