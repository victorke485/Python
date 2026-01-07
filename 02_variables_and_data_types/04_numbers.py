num1 = 126
num2 = 34.04

print(f"{num1} is of type: {type(num1)}")
print(f"{num2} is of type: {type(num2)}")

print(f"{num1} + {num2} = {num1 + num2}") # Addition
print(f"{num1} - {num2} = {num1 - num2}") # Substraction
print(f"{num1} * {num2} = {num1 * num2}") # Multiplication
print(f"{num1} / {num2} = {num1 / num2}") # Division
print(f"{num1} % {num2} = {num1 % num2}") # Modulus - returns remainder
print(f"{num1} // {num2} = {num1 // num2}") # Floor division
print(f"{num1} ** {num2} = {num1 ** num2}") # Exponential

# Returning a floating-point number
print(float(543))

# Returning an integer
print(int(12.54))

# round() - rounds a number to the specified number of decimal place
print(round(12.999))
print(round(12.1289, 3))

# abs() - returns the absolute value of a number
print(abs(-211))
print(abs(31))

# pow() - raises a number to the power of another
print(pow(9, 2))
