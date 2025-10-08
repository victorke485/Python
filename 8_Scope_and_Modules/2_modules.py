import mymodule

mymodule.greeting("Victor")

# Renaming a module
import mymodule as test

test.greeting("Mutua")

# Import parts of module
from mymodule import languages

print(languages[0])

# dir() function - lists all the function names in a module
print(dir(mymodule))
