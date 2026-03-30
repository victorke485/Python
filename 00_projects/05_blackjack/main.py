from art import logo
import random, os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_game = True

def ace(deck):
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)

def blackjack(player_cards, computer_cards):
    if sum(player_cards) > 21:
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("You went over. You lose 😭")
    else:
        while sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))

        ace(computer_cards)
        
        if sum(computer_cards) > 21:
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("Computer went over. You win 😊")
        elif sum(computer_cards) < sum(player_cards):
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("You win 😊")
        elif sum(computer_cards) == sum(player_cards):
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("Its a draw")
        else:
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("You Lose 😭")


while continue_game:
    os.system("clear")

    player_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards)]
    get_card = True
    print(logo)

    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    while get_card:
        add_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if add_card == "y":
            player_cards.append(random.choice(cards))
            ace(player_cards)
            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
        else:
            get_card = False

        if sum(player_cards) > 21:
            get_card = False
    
    blackjack(player_cards, computer_cards)

    play_again = input("Type 'y' to play again and 'n' to exit: ").lower()

    if play_again != "y":
        continue_game = False


