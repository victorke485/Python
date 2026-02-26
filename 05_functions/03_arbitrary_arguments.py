# Arbitrary Positional Arguments - allow functions to accept any numbe of arguments
# * converts arguments to a single iterable(tuple) --args
def average(*values):
     return(sum(values) / len(values))

numbers = [2, 3, 4, 12, 34]
print(average(*numbers))
print(average(21, 11, 34, 45, 46))



# Arbitrary KeyWord Arguments
# ** --kwargs
def average2(**v):
     return(sum(v.values()) / len(v.values()))

num_dict = {
     "A": 23,
     "B": 53,
     "C": 64,
     "D": 75
}
print(average2(**num_dict)) 