from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:

    choice = input(f"What would you like?: ({menu.get_items()}) ")

    if choice == "off":
        is_on = False
    
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()

    else:
        # choice in menu.get_items().split("/"):
        item = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
                coffe_maker.make_coffee(item)
                
    
   






 
        


        
        




    
    

































    

    





