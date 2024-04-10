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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# # TODO 3 Print Report
def print_report(resource, money):
    """shows the remaining resources available"""
    print(f"""
    Water: {resource['water']}
    Milk: {resource["milk"]}
    Coffee: {resource["coffee"]}
    Money: {money}
    """)


def is_resource_sufficiency(order_ingredients):
    """Return True or False based on Resource availability"""
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print(f'Sorry there is not enough {items}')
            return False
    return True


def make_coffee(resource, option, coin_received):
    """input choices and coins and update resources and return change money"""
    for items in MENU[option]['ingredients']:
        resource[items] -= MENU[option]['ingredients'][items]
    global MONEY
    MONEY += MENU[option]['cost']
    return round(coin_received - MENU[option]['cost'], 2)


def count_coins():
    """Takes money from customer and sum up to dollar"""
    print("Please insert coins")
    total = int(input("How many Quarters? : ")) * 0.01
    total += int(input("How many Dimes? : ")) * 0.1
    total += int(input("How many nickels? : ")) * 0.05
    total += int(input('How many pennies? : ')) * 0.25
    return total


def refill_machine():
    global resources
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    print('Machine is Ready for more!!')


MONEY = 0
is_on = True

while is_on:
    # TODO 1 ask user the choice
    choice = input("What would you like? (espresso/latte/cappuccino) : ")

    # TODO 2 Turn off the Coffee Machine by entering "off" to the prompt.
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print_report(resources, MONEY)
    elif choice == 'refill':
        refill_machine()

    elif choice in ['latte', 'cappuccino', 'espresso']:
        if is_resource_sufficiency(MENU[choice]['ingredients']):
            coins_received = count_coins()
            if coins_received < MENU[choice]['cost']:
                print("Sorry that's not enough  Money, Money Refunded.")
            else:
                return_change = make_coffee(resources, choice, coins_received)
                if return_change != 0:
                    print(f"Here is ${return_change} in change")

                print(f"Here is your {choice} ☕️. Enjoy! 😊")
