# Docstring - is a block of string used to descibe a function

# Accessing docstring:
# print(help(round))

# Acccessing only the docstring
print(round.__doc__)

# Creating a docstring
def average(values):
    """Find the mean in a sequence of values and round to two decimal places."""
    average_value = sum(values) / len(values)
    rounded_average = round(average_value, 2)
    return rounded_average

print(average.__doc__)

# Updating a function's docstring
average.__doc__ = "Calculate the mean of values in a dara structure, rounding the result to 2 digits."

print(average.__doc__)
