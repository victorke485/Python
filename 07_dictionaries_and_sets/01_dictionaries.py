# Are built-in data structures that store collections of key-value pairs
# Syntax:
person = {
    "name": "Victor",
    "age": 33,
    "hobbies": ["chess", "coding"]
}


# print(type(person))
# print(person)

# print(f"Name: {person["name"]}\nAge: {person['age']}\nHobbies: {person['hobbies'][1]}")

# dict() constructor
# pizza = dict([("name", "Margheritta Pizza"), ("Price", 12)])
# print(pizza)

# Updating value
# person["age"] = 22
# print(person["age"])

# .get() method - retrieves the value associated with a key
# print(person.get("age"))
# Advantage of .get() is that you don't get an error if the key does not exist

# .keys(), .values() and .items() methods
# print(person.keys())
# print(person.values())
# print(person.items())

# .clear() - removes all the key-value pairs from the dictionary
# person.clear()

# .pop() - removes the key-value pair with the key that you specify
# person.pop("age")

# .popitem() - removes the last inserted item
# person.popitem()

# .update() - updates the ket-value pair with the key-value pair of another dictionary
person.update({
    "age": 55,
    "profession": "developer"
})


print(person)