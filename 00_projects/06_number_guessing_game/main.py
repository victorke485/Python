from art import logo
import random
import os

def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "hard":
        return 5
    elif difficulty =="easy":
        return 10
    else:
        print("Invalid choice, defaulting to easy.")
        return 10

def game(attempts, random_number, guess_number):
    while attempts > 0 and random_number != guess_number:
        print(f"You have {attempts} attempts remaining to guess the number.")
            
        try:
            guess_number = int( input("Make a guess: ") )
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not 1 <= guess_number <= 100:
            print("Please guess a number between 1 and 100.")
            continue

        attempts -= 1

        if guess_number == random_number:
            print(f"You got it! The answer was {random_number}.")
        elif guess_number > random_number:
            print("Too high.")
        else:
            print("Too low.")
    
    if guess_number != random_number:
        print(f"You've run out of guesses. The number was {random_number}")

is_over = False

while not is_over:
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")   

    random_number = random.randint(1, 100)
    guess_number = 0
    attempts = choose_difficulty()
    
    game(attempts, random_number, guess_number)
        
    play_again = input("Enter 'y' to play again or 'n' to exit: ").lower()

    if play_again != "y":
        is_over = True
