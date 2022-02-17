from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

running = True

menu = Menu()
machine = CoffeeMaker()
cash_handelar = MoneyMachine()


while running:
    choice = input(f"What would you like? ({menu.get_items()}):")
    if choice == "off":
        print("Machine is OFF")
        running = False
    elif choice == "report":
        print("Report\n")
        machine.report()
        cash_handelar.report()
    else:
        drink = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink) and cash_handelar.make_payment(drink.cost):
            machine.make_coffee(drink)