from hangman_words import word_list
from hangman_art import stages, logo

import random

print(logo)

random_word = random.choice(word_list)
guessed_word = "_"*len(random_word)
guessed_letters = ""
game_over = False
lives = 6

print(random_word)
print(f"Word to guess: {'_ '*len(random_word)}")

while not game_over:
    guess = input("Guess a letter: ").lower()
    guessed_word = list(guessed_word)

    if guess in guessed_letters:
        print(f"You have already guessed {guess}! Try another letter")

    elif guess in random_word:
        guessed_letters += guess
        letter_index = 0
        for i in random_word:
            if i == guess:
                guessed_word[letter_index] = guess
            letter_index += 1
        guessed_word = "".join(guessed_word)
        if guessed_word == random_word:
            game_over = True
            print(f"You Win! The word was {guessed_word}")
        else:
            print(guessed_word)
            print(stages[lives])
            print(f"****************************{lives}/6 LIVES LEFT****************************")

    else:
        lives -= 1
        guessed_letters += guess
        if lives == 0:
            print(f"***********************IT WAS {random_word}! YOU LOSE**********************")
            print(stages[lives])
            game_over = True
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print(stages[lives])
            print(f"****************************{lives}/6 LIVES LEFT****************************")
            print(guessed_word)
