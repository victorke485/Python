import os, time

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    os.system("cls" if os.name == "nt" else "clear")
    options = menu.get_items()
    coffee_type = input(f"What would you like? ({options}): ").lower()
    while coffee_type not in ["off", "report", "espresso", "latte", "cappuccino"]:
        coffee_type = input(f"Please enter a valid option. What would you like? ({options}): ").lower()
    
    if coffee_type == "report":
        coffee_maker.report()
        money_machine.report()
    elif coffee_type == "off":
        is_on = False
    else:
        drink = menu.find_drink(coffee_type)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    
    time.sleep(3)