from data import MENU, resources

running = True
profit = 0


def check_resources(ingredients):
    for item in ingredients:
        if resources[item] < ingredients[item]:
            return False
    return True


def make_drink(items):
    for item in items:
        resources[item] -= items[item]
    global profit
    profit += MENU[choice]["cost"]
    print("Here is your drink. Enjoy! ")

def count_money(cost):
    total = int(input("How many 1$: "))
    total += int(input("How many 50 cents: "))*0.5
    total += int(input("How many 20 cents: "))*0.2
    total += int(input("How many 10 cents: ")) * 0.1
    total += int(input("How many 5 cents: ")) * 0.05

    if cost > total:
        print("Not sufficient money. here is your money ")
        return False
    else :
        print(f"you entered ${total} here is your ${round(total-cost,2)}return")
        return True


while running:

    choice = input("What drink would you like to have (espresso/latte/cappuccino) :")

    if choice == "off":
        running = False

    elif choice == "report":
        for item in resources:
            print(f"{item} : {resources[item]} ")
        print(f"money: {profit}")

    else:
        if check_resources(MENU[choice]["ingredients"]) and count_money(MENU[choice]["cost"]):
            make_drink(MENU[choice]["ingredients"])
