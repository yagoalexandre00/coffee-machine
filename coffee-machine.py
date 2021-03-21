# Coffee Machine
# Author >>> Yago Goltara

from resources import MENU, resources
from os import system
from time import sleep

def enter_function():
    """
    Display a input() and after that, clean the screen
    """
    sleep(1)
    input("Press 'ENTER' to continue...")
    system('cls')

def ingredients_checker(option):
    """
    Display the ingredients
    """
    ingredients_esp = MENU['espresso']['ingredients']
    ingredients_lat = MENU['latte']['ingredients']
    ingredients_cap = MENU['cappuccino']['ingredients']
    
    if option == 3:
        for ingredient in ingredients_esp:
            if 'coffee' not in ingredient:
                print(f"| {ingredient}: {ingredients_esp[ingredient]} ml")
            else:
                print(f"| {ingredient}: {ingredients_esp[ingredient]} g")
    elif option == 2:
        for ingredient in ingredients_lat:
            if 'coffee' not in ingredient:
                print(f"| {ingredient}: {ingredients_lat[ingredient]} ml")
            else:
                print(f"| {ingredient}: {ingredients_lat[ingredient]} g")
    elif option == 1:
        for ingredient in ingredients_cap:
            if 'coffee' not in ingredient:
                print(f"| {ingredient}: {ingredients_cap[ingredient]} ml")
            else:
                print(f"| {ingredient}: {ingredients_cap[ingredient]} g")
    elif option == 4:
        for current_resources in resources:
            if 'coffee' not in current_resources:
                print(f"| {current_resources}: {resources[current_resources]} ml")
            else:
                print(f"| {current_resources}: {resources[current_resources]} g")
    else:
        print("Please, type a valid command.")

def drink_value(drink):
    """
    Check the drink's value and return it
    """
    cap_value = MENU['cappuccino']['cost']
    lat_value = MENU['latte']['cost']
    esp_value = MENU['espresso']['cost']

    if drink == 1:
        return cap_value
    elif drink == 2:
        return lat_value
    elif drink == 3:
        return esp_value

def drink_check(option):
    """
    Check if there are enough ingredients to make the drink choosen. If so, go to payment() function
    """
    ingredients_esp = MENU['espresso']['ingredients']
    ingredients_lat = MENU['latte']['ingredients']
    ingredients_cap = MENU['cappuccino']['ingredients']


    if option == 1:
        if not (ingredients_cap['coffee'] > resources['coffee'] or ingredients_cap['water'] > resources['water'] or ingredients_cap['milk'] > resources['milk']):
            resources['coffee'] -= ingredients_cap['coffee']
            resources['water'] -= ingredients_cap['water']
            resources['milk'] -= ingredients_cap['milk']
            return True


    elif option == 2:
        if not (ingredients_lat['coffee'] > resources['coffee'] or ingredients_lat['water'] > resources['water'] or ingredients_lat['milk'] > resources['milk']):
            resources['coffee'] -= ingredients_lat['coffee']
            resources['water'] -= ingredients_lat['water']
            resources['milk'] -= ingredients_lat['milk']
            return True


    elif option == 3:
        if not (ingredients_esp['coffee'] > resources['coffee'] or ingredients_esp['water'] > resources['water']):
            resources['coffee'] -= ingredients_esp['coffee']
            resources['water'] -= ingredients_esp['water']
            return True
 
    return False
        
    
def payment():
    """
    Payment session which deals with coins and return the sum of their input()
    """
    print("\t|PAYMENT SESSION|")
    print(f"| Final bill: ${drink_value(drink)}")
    quarters = int(input("| How many QUARTERS: ")) 
    dimes = int(input("| How many DIMES: "))
    nickles = int(input("| How many NICKLES: "))
    pennies = int(input("| How many PENNIES: "))
    final_amount = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01

    return final_amount



option = 0          # Starter flag

while option != 4:

    option = int(input("\t|COFFEE MACHINE|\n| (1) - Buy a drink\n| (2) - Check current resources\n| (3) - Check drink's ingredients\n| (4) - Exit\n| Option >>> "))
    system('cls')

    if option == 1:
        print("\t|BUY A DRINK|")
        drink = int(input("| What would you like?\n| (1) - Cappuccino\n| (2) - Latte\n| (3) - Espresso\n| Enter >>> "))
        available = drink_check(drink)  
        enter_function()

        if available == True:
            final_bill = payment()
            drink_cost = drink_value(drink)
            if final_bill >= drink_cost:
                final_bill -= drink_cost 
                print("| We're preparing your drink!")
                sleep(1.3)
                print(f"| It's done! You still have ${final_bill}")
            else:
                print("| Oops... There's not enough money. Money refunded.")

        else:
            print("There aren't available resources at the moment. Please come back later.")
        enter_function()

    elif option == 2:
        print("\t|CURRENT RESOURCES|\n")
        ingredients_checker(4)
        enter_function()

    elif option == 3:
        print("\t|INGREDIENTS CHECKER|")
        drink = int(input("| Which drink would you like to view its ingredients?\n| (1) - Cappuccino\n| (2) - Latte\n| (3) - Espresso\n| Enter >>> "))
        ingredients_checker(drink)
        enter_function()

    elif option == 4:
        print("\t|COFFEE MACHINE|\n| Bye bye. See you later!")
        enter_function()

    else:
        print("Please, insert a valid command.")


# Hope you all have fun with this code.
# I particularly had a lot.
# Feel free to take it to you and change what you want. 