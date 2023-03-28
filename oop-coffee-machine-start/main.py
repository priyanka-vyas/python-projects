from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine=CoffeeMaker()
#type(coffee)
menu=Menu()
menu_item=MenuItem()
money=MoneyMachine()
turn=True
while turn:
    options=menu.get_items()
    choice=input(f"What would you like to have{options}")
    if choice=="off":
        turn = False
    elif choice=="report":
        machine.report()
        money.report()
    else:
        drink=menu.find_drink(choice)
        if machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            machine.make_coffee(drink)
        else:
            turn= False












