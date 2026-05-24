# List comprehension allows you to create a new list in a single line by combining a loop and comdition directly within square brackets
even_numbers = [num for num in range(21) if num % 2 == 0]
# print(even_numbers)
result = [(num, "Even") if num % 2 == 0 else (num, "Odd") for num in range(10)]
# print(result)

# filter() function - used to select an element from an iterable that meets a specific condition
# Accepts a function and an iterable for its arguments
words = ["Cart", "tree", "Mountain", "Laptop", "River", "Cloud", "Sun"]

def is_long_word(word):
    return len(word) > 4
long_words = list(filter(is_long_word, words))
# print(long_words)

# map() function - takes an iterable and applies a function to each of its elements
celsius = [0, 10, 20, 30, 40]


def to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


fahrenheit = list(map(to_fahrenheit, celsius))
# print(fahrenheit)

# sum() function
# Syntax: sum(iterable, start)
numbers = [3, 4, 4, 5, 6]
# print(sum(numbers, 10))

# Nested lists
pair_numbers = [(num_1, num_2) for num_1 in range(1, 6) for num_2 in range(6, 11)]
print(pair_numbers)

pair_numbers = list(zip(range(1, 6), range(6, 11)))
print(pair_numbers)