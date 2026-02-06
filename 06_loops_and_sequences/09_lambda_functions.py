# Are inline functions
# Are anonymous
numbers = [2, 23, 22, 10]
even_numbers = list(filter(lambda x: x % 2 ==0, numbers))
print(even_numbers)

add = lambda x, y: x + y
print(add(2, 4))

odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
print(odd_numbers)