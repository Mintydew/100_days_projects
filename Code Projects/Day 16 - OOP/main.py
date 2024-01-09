# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

machine_active = True
menu_item = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while machine_active:
    user_input = input(f"what would you like? ({menu_item.get_items()})")

    if user_input == "off":
        print("Turning off machine")
        machine_active = False

    elif user_input == "report":
        coffee_machine.report()
        money_machine.report()

    else:
        user_drink = menu_item.find_drink(user_input)

        if coffee_machine.is_resource_sufficient(user_drink):
            if money_machine.make_payment(user_drink.cost):
                coffee_machine.make_coffee(user_drink)
