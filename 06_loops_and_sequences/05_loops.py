import random
# for loop
programming_languages = ["Rust", "Java", "Python", "C++"]

for language in programming_languages:
    print(language)

# nested loops
categories = ("Fruits", "Vegetable")
foods = ("Apple", "Carrot", "Banana")

for category in categories:
    for food in foods:
        print(category, food)

# while loop - repeats a block of code until a condition is False
secret_number = random.randint(0, 9)
print(secret_number)
guess = 0

while guess != secret_number:
    guess = int(input("Enter a random number: "))
    if guess != secret_number:
        print("Wrong! Try again")
    if guess == 4:
        print(secret_number)
        # continue
        break


# for else
words = ["sky", "apple", "rhythm", "fly", "orange"]

for word in words:
    for letter in word:
        if letter.lower() in "aeiou":
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")
