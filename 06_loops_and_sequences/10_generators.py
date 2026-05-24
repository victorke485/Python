# Generator objects 
numbers = (n for n in range(100000000000000000000000000000000000))
# print(numbers)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

# Generator function - is the funtion definition that uses yield
def num_sequence(n):
    """Generates numbers from 0 to n"""
    i = 0
    while i < n:
        yield i
        i += 1

result = num_sequence(11)
print(next(result))
print(next(result))
print(next(result))

# for number in sequence4:
#     print(number)

remaining = list(result)
print(remaining)

# Advantages of generators:
# -Memory efficient
# -Lazy evaluation - do work only when asked
# -Handling large/infinite data streams cleanly