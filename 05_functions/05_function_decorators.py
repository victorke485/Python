import time

# Decorator function is a function that wraps a function and gives it additional functionality or modifies its functionality
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")

say_hello()