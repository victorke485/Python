# F-Strings
age = 18
txt = f"My name is victor , I am {age}"
print(txt)

# Placeholders and Modifiers
price = 79
txt1 = f"The price is {price:.2f} dollars"
print(txt1)

# Placeholders can also contain python code
print(f"The price of 10 packets is {(12 * 20):.2f} dollars")