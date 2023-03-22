class CoffeeMaker:
    """Models the machine that makes the coffee"""

    REFILL_AMOUNT = 100

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

        self.max_resources = {
            "water": 1000,
            "milk": 500,
            "coffee": 200,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False
         if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

    def refill(self, choice):
        """Refills the given resource"""
        if choice in self.resources:
            if self.resources[choice] + self.REFILL_AMOUNT > self.max_resources[choice]:
                print(
                    f"Can't refill. Max of {choice}" +
                    " is {self.max_resources[choice]}")
            else:
                unit = "g" if choice == "coffee" else "ml"
                print(f"Refilling {choice} by {self.REFILL_AMOUNT}{unit}")
                self.resources[choice] += self.REFILL_AMOUNT
        else:
            print("No resource to refill")
