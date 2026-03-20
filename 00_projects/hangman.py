import random
print(
    """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
"""
)

random_words = ["Arsenal", "Python", "Chelsea"]
random_word = random.choice(random_words).lower()
print(random_word)

guessed_word = "_" * len(random_word)
print(f"Word to guess: {guessed_word}")

guessed_word_list = list(guessed_word)
random_word_list = list(random_word)
lifes = 6

while not(lifes == 0 or guessed_word == random_word):
    guess = input("Guess a letter: ").lower()
    if guess in random_word_list:
        guessed_word_list[random_word_list.index(guess)] = guess
        random_word_list[random_word_list.index(guess)] = "-"
        guessed_word = "".join(guessed_word_list)
        print(guessed_word)

    else:
        print(f"{guess} is not in word")
        lifes -= 1
        print(f"You have {lifes}/6 lifes remaining")
        if lifes == 5:
            print(
                """
  +---+
  |   |
  O   |
      |
      |
      |"""
            )
        elif lifes == 4:
            print(
                """
  +---+
  |   |
  O   |
  |   |
      |
      |"""
            )
        elif lifes == 3:
            print(
                """
  +---+
  |   |
  O   |
 /|   |
      |
      |"""
            )
        elif lifes == 2:
            print(
                """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |"""
            )
        else:
            print(
                """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |""")
            print("IT WAS joyful! YOU LOSE")
