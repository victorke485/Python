import os, time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def check_requirements(coffee_type, resources):
    enough_water = resources["water"] >= MENU[coffee_type]["ingredients"]["water"]
    enough_coffee = resources["coffee"] >= MENU[coffee_type]["ingredients"]["coffee"]

    if coffee_type != "espresso":
        enough_milk = resources["milk"] >= MENU[coffee_type]["ingredients"]["milk"]
    else:
        enough_milk = True

    if enough_milk and enough_coffee and enough_water:
        return True
    else:
        if not enough_water:
            print("Sorry there is not enough water.")
        if not enough_milk:
            print("Sorry there is not enough milk.")
        if not enough_coffee:
            print("Sorry there is not enough coffee.")
        
        return False


def get_coins(coffee_type, MENU):
    while True:
        try:
            quarters = int(input("How many quarters?:"))
            dimes = int(input("How many dimes?:"))
            nickles = int(input("How many nickles?:"))
            pennies = int(input("How many pennies?:"))
            break
        except ValueError:
            print("Please enter amount of coins using numbers only")
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    if total < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total == MENU[coffee_type]["cost"]:
        return True
    else:
        print(f"Here is ${round(total - MENU[coffee_type]['cost'], 2)} dollars in change.")
        return True


def make_coffee(coffee_type, resources):
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_type != "espresso":
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    
    print(f"Here is your {coffee_type} ☕ Enjoy!")

still_on = True

while still_on:
    os.system("cls" if os.name == "nt" else "clear")
    action = input("What would you like? (espresso/latte/cappuccino): ").lower()

    while action not in ["espresso","latte","cappuccino","report", "off"]:
        action = input("Invalid Option! \n What would you like? (espresso/latte/cappuccino): ").lower()

    if action == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    elif action == "off":
        still_on = False
        continue
    else:
        if check_requirements(action, resources):
            if get_coins(action, MENU):
                make_coffee(action, resources)
                profit += MENU[action]["cost"]
    time.sleep(5)