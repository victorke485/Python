# Python Dates
import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# The strftime() Method
x = datetime.datetime.now()
print(x.strftime("%A"))