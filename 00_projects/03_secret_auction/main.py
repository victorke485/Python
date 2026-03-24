from art import logo
import os

print(logo)

bids = {}

def get_bid():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid

over = False

while not over:
    get_bid()
    other_bids = input("Are there any other bidders? Type 'yes or 'no'. ")
    if other_bids == "no":
        over = True
    else:
        _ = os.system("clear")

winner = max(bids, key=bids.get)
print(f"The winner is {winner} with a bid of ${bids[winner]}")
