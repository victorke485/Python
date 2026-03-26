from art import logo
import random, os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_game = True

while continue_game:
    os.system("clear")
    print(logo)
    player_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards)]
    get_card = True

    while sum(player_cards) < 21 and sum(computer_cards) < 21:
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(
            f"Computer's cards: {computer_cards} , current score: {sum(computer_cards)}"
        )

        add_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if add_card == "y":
            player_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
        else:
            computer_cards.append(random.choice(cards))

    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}"
    )

    if (sum(player_cards) < 21 and sum(player_cards) > sum(computer_cards)) or sum(computer_cards) > 21:
        print("You win 😁")
    else:
        print("You lose 😤")

    continue_g = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    ).lower()

    if continue_g != "y":
        continue_game = False

