# Types of error: TypeError, ValueError

def average(values):
    try:
        return sum(values) / len(values)
    except:
        print("Please provide an iterable data structure")
print(average("we"))
print(average([12, 23, 43]))


# raise
def average_2(values):
    if type(values) in [list, set]:
        return sum(values) / len(values)
    else:
        raise TypeError("Please provide an iterable data structure")

print(average_2("we"))
print(average_2([12, 23, 43]))
