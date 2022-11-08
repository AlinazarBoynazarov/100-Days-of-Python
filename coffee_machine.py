
def report():
    status = {
        "Water": 1000,
        "Milk": 600,
        "Coffee": 400,
        "Money": 0
    }

    return status


def reqs():
    latte = {
        "Water": 200,
        "Milk": 300,
        "Coffee": 200
    }

    espresso = {
        "Water": 200,
        "Milk": 400,
        "Coffee": 100
    }

    cappuccino = {
        "Water": 300,
        "Milk": 300,
        "Coffee": 150
    }

    return latte, espresso, cappuccino


def check_resources(answer, lat, espr, cappuc, stat):
    
    lacking_resources = []
    coffe_to_be_made = {}

    if answer == "latte":
        coffe_to_be_made = lat
    elif answer == "espresso":
        coffe_to_be_made = espr
    elif answer == "cappuccino":
        coffe_to_be_made = cappuc

    for key in coffe_to_be_made:
        if key in stat:
            if coffe_to_be_made[key] > stat[key]:
                lacking_resources.append(key)
        # elif key not in stat:
        #     pass

    if lacking_resources:
        print(f"Sorry, we don't have enough: {', '.join(lacking_resources)}")
        return False

    return True


def cost():

    cost_dict = {

        "latte": 2.50,
        "espresso": 1.5,
        "cappuccino": 3

    }

    return cost_dict


def coins():
    quarters = float(input("How many quarters? ")) * 0.25
    dimes = float(input("How many dimes? ")) * 0.10
    nickles = float(input("How many quarters? ")) * 0.05
    pennies = float(input("How many pennies? ")) * 0.01

    value = sum([quarters, dimes, nickles, pennies])

    return value


def main():
    should_continue = True

    latte, espresso, cappuccino = reqs()
    status = report()

    while should_continue:

        prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if prompt == "report":
            for key in status:
                print(f" {key}: {status[key]}")

        elif prompt == "off":
            should_continue = False

        elif prompt == "latte" or prompt == "cappuccino" or prompt == "espresso":
            if check_resources(prompt, latte, espresso, cappuccino, status) == True:
                print("Please insert coins.")

                value = coins()
                cost_dict = cost()
                price = cost_dict[prompt]

                if value < price:
                    print("Sorry that's not enough money. Money refunded. 🥱")
                elif value > price:
                    status["Money"] += price
                    change = value - price

                    print(f"Here is ${round(change, 2)} dollars in change. 🤑")

                    # deducting from the status dictionary
                    coffee = {}

                    if prompt == "latte":
                        coffee = latte
                    elif prompt == "espresso":
                        coffee = espresso
                    elif prompt == "cappuccino":
                        coffee = cappuccino

                    for key in status:
                        if key in coffee:
                            status[key] -= coffee[key]

                    for key in status:
                        print(f"{key}: {status[key]}")

                    print(f"Here is your {prompt}. Enjoy! 😉")
        
        else:
            print("Please input the appropriate values 🤬")
                
main()
