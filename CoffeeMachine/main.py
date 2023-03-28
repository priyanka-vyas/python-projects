MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money=0.0
machine_state=True

def sufficient_resources(ingredients):
    for i in ingredients:
        if ingredients[i]>resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def calculate_coins():
    #quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    print("Insert coins")
    coins=int(input("How many Quarters"))*0.25
    coins+=int(input("How many dimes"))*0.10
    coins+=int(input("How many nickles"))*0.05
    coins+=int(input("How many pennies"))*0.01
    return coins

def deduct_resources(ingredients):
    for i in ingredients:
        resources[i]-= ingredients[i]

while machine_state:
    coffee=input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffee == "off":
        machine_state = False
    elif coffee == "report":
        for i in resources:
            print(f"{i}:{resources[i]}")
        print(f"money:${money}")
    else:
        drink=MENU[coffee]
        if sufficient_resources(drink["ingredients"]):
            coins=calculate_coins()
            if coins<drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif coins>=drink['cost']:
                if coins>drink['cost']:
                    change=coins-drink['cost']
                    print(f"Here is ${'%.2f' %change} dollars in change.")
                money=drink['cost']
                deduct_resources(drink["ingredients"])
                print(f"Here is your{coffee}☕. Enjoy")






# def sufficient_resources(coffee):
#     if coffee=="espresso":
#         if resources["water"]<50:
#             print("Sorry there is not enough water.")
#         if resources["coffee"]<18:
#             print("Sorry there is not enough coffee.")
#         if money<1.5:
#             print("Sorry there is not enough Money.Money refunded.")
#     elif coffee=="latte":
#         if resources["water"]<200:
#             print("Sorry there is not enough water.")
#         if resources["coffee"]<24:
#             print("Sorry there is not enough coffee.")
#         if resources["milk"]<100:
#             print("Sorry there is not enough milk.")
#         if money<2.5:
#             print("Sorry there is not enough Money.Money refunded.")
#     elif coffee == "cappuccino":
#         if resources["water"] < 250:
#             print("Sorry there is not enough water.")
#         if resources["coffee"] < 24:
#             print("Sorry there is not enough coffee.")
#         if resources["milk"] < 100:
#             print("Sorry there is not enough milk.")
#         if money < 3.0:
#             print("Sorry there is not enough Money.Money refunded.")