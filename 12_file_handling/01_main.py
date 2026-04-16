file = open("12_file_handling/my_file.txt")
contents = file.read()
print(contents)
file.close()

# Best practice
with open("12_file_handling/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Mode: a(append), w(write), r(read)
with open("12_file_handling/my_file.txt", mode="a") as file:
    file.write("\nNew text")


# Creating new file
with open("12_file_handling/new_file.txt", mode="w") as file:
    file.write("This is a new file that has been created")
