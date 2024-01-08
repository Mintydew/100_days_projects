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

machine_active = True
total = 0

# TODO: Check resources sufficient?


def resource_check(user_drink):
    ingredient_resources = MENU[user_drink]["ingredients"]

    for key, item in ingredient_resources.items():
        if key in resources and item > resources.get(key):
            print(f"Sorry there is not enough {key}")
            return False

    return True


def money_input(current_fund=0):
    print("Please insert coins.")
    quarters_count = input("How many quarters?")
    dimes_count = input("How many dimes?")
    nickles_count = input("How many nickles?")
    pennies_count = input("How many pennies?")

    quarters_count = quarters_count if quarters_count else 0
    dimes_count = dimes_count if dimes_count else 0
    nickles_count = nickles_count if nickles_count else 0
    pennies_count = pennies_count if pennies_count else 0

    total_calc = float(quarters_count) * 0.25 + float(dimes_count) * 0.1 + float(nickles_count) * 0.05 + float(pennies_count) * 0.01 + current_fund
    print(f"You have: ${total_calc}")
    return total_calc


def transaction_check(user_drink, received_fund):
    cost = MENU[user_drink]["cost"]

    if received_fund < cost:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        returning_money = round(received_fund - cost, 2)
        print(f"\nYou now have ${returning_money} in change")
        return returning_money


def update_resource(user_drink):
    ingredient_resources = MENU[user_drink]['ingredients']

    for key, value in resources.items():
        if key in ingredient_resources:
            resources[key] = value - ingredient_resources[key]

    print(f"Here is your {user_drink}. Enjoy!")

# TODO: 1. Print Report of all coffee machine resources

while machine_active is True:
    user_input = input("What would you like? (espresso/latte/cappuccino):")

    if user_input == "off":
        print("Goodbye")
        machine_active = False
        break

    elif user_input == "report":
        iteration = iter(resources.items())

        water_item, water_cost = next(iteration)
        milk_item, milk_cost = next(iteration)
        coffee_item, coffee_cost = next(iteration)

        print(f"{water_item.title()}: {water_cost}ml")
        print(f"{milk_item.title()}: {milk_cost}ml")
        print(f"{coffee_item.title()}: {coffee_cost}g")
        print(f"Money: ${total}")

    elif user_input in MENU.keys():
        drink = user_input
        print(f"You ordered an: {drink.title()}.")

        if resource_check(drink):
            print(f"Your drink will cost ${MENU[drink]['cost']}")
            total = money_input(total)

            if transaction_check(drink, total):
                total = transaction_check(drink, total)
                update_resource(drink)
                print("")

