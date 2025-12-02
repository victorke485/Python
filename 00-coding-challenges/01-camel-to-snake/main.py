# Given a string in camel case, return the snake case version of the string using the following rules:
"""
The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).
"""


def to_snake(camel):
    camel = list(camel)
    snake = []

    for x in camel:
        if x.isupper():
            snake.append("_")
        snake.append(x)

    snake = "".join(snake).lower()
    return snake

print(to_snake("helloWorld"))
print(to_snake("myVariableName"))
print(to_snake("freecodecampDailyChallenges"))
