from art import logo, vs
from game_data import data
import random
import os    

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)

def get_b(a):
    b = random.choice(data)

    while a == b:
        b = random.choice(data)
    return b

game_running = True

while game_running:
    clear_screen()
    round_over = False
    score = 0

    while not round_over:  
        if score == 0:
            option_a = random.choice(data)
            option_b = get_b(option_a)
        else:    
            option_a = option_b
            option_b = get_b(option_a)
            clear_screen()
            print(f"You're right! Current score: {score}.")

        print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
        print(vs)
        print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

        guess = ""
        while guess not in ["a", "b"]:
            guess = input("Please type 'A' or 'B': ").lower()
        a_win = option_a["follower_count"] >= option_b["follower_count"]
        if (guess == "a" and a_win) or (guess == "b" and not a_win):
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            round_over = True

    play_again = input("Enter 'y' to play again or 'n' to exit: ").lower()

    if play_again != "y":
        game_running = False

        
