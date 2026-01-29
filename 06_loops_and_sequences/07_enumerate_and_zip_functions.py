# enumarate() function keeps track of the index for an iterable and returns an enumerate object
languages = ["Python", "Java", "Javascript", "C"]

for index, language in enumerate(languages, 3):
    print(f"Index: {index} and language: {language}")


# zip() function is used to iterate multiple lists in parallel
ids = [1, 2, 3, 4]
names = ["Victor", "Alex", "Job", "Peter"]

for name, id in zip(names, ids):
    print(f"Name: {name}, ID: {id}")