# Represents an anonymous function
# Syntax: lambda argument : expression
# Can also be stored as variables to be used later

print((lambda x: sum(x) / len(x))([2, 4, 5]))

# Storing lambda function as an variable
average = lambda x: sum(x) / len(x)
print(average([4, 6]))

# Multiple parameters
power = lambda x, y: x**y
print(power(3, 68))
print(power(9, 34))
print(power(81, 17))

# Lambda functions with iterables
# map() --> Applies a function to all elements in an iterable
names = ["alex", "kim", "brian"]
to_upper = map(lambda x : x.upper(), names)
print(list(to_upper))