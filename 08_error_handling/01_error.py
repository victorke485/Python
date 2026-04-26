# Types of error: TypeError, ValueError


def average(values):
    try:
        return sum(values) / len(values)
    except:
        print("Please provide an iterable data structure")


# print(average("we"))
print(average([12, 23, 43]))


# raise
def average_2(values):
    if type(values) in [list, set]:
        return sum(values) / len(values)
    else:
        raise TypeError("Please provide an iterable data structure")


# print(average_2("we"))
print(average_2([12, 23, 43]))

# try except
try:
    a_dictionary = {"name": "victor"}
    print(a_dictionary["score"])
except KeyError:
    print("That key does not exist")

# try, except, else, finally
try:
    file = open("sfile1.txt")
except FileNotFoundError as error_message:
    print(f"An error occured: {error_message}")
    file = open("sfile1.txt", "w")
else: # gets execured if no error occured
    print("No error occured")
finally:
    file.close()
    print("File was closed")