# JSON is syntax for storing and exchanging data
# JSON in Python
import json

# Parse JSON - Convert from JSON to Python
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["name"])

# Convert from Python to JSON
z = json.dumps(y)
print(z)

# Format the results
q = json.dumps(y, indent=4)
print(q)