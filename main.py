from menu import Menu
from coffee_maker import CoffeeMaker
from cashier import Cashier

cashier = Cashier()
coffee_maker = CoffeeMaker()
menu = Menu()

IS_ON = True

while IS_ON:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        IS_ON = False
    elif choice == "report":
        coffee_maker.report()
        cashier.report()
    elif choice == "refill":
        refill_item = input("What to refill (water / milk / coffee): ")
        coffee_maker.refill(refill_item)
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and cashier.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
