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
is_on = True

max_resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 200,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def refill(choice):
    if choice in resources:
        if resources[choice] + 100 > max_resources[choice]:
            print(f"Can't refill. Max of {choice} is {max_resources[choice]}")
        else:
            print(f"Refilling {choice}")
            resources[choice] += 100
    else:
        print("No resource to refill")


def serve_change(change):
    if change != 0:
        print(f"Here is {change}$ in change.")


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted,
    or False if payment is not accepted"""
    if money_received >= drink_cost:
        serve_change(money_received - drink_cost)
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


def is_resource_sufficient(order_ingredients):
    """Check if there is sufficient resources.
    If not returns False. If yes returns True."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calc from coins intesrted."""
    print("Please insert coins.")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


def make_coffee(drink):
    """Deduct the required ingredient from the resuources"""
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} ☕")


while is_on:
    choice = input("What would you like? "
                   + "(espresso / latte / cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "refill":
        refill_item = input("What to refill (water / milk / coffee): ")
        refill(refill_item)
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: {profit}$")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice)
