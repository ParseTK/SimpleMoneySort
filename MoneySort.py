from decimal import Decimal

# create main
# Create a menu for the simple money sort
# get user choice
# perform making change for a specified amount
# track total inventory change for the day
# reset the program

# -------+ TO DO +-------
# Finish logic for main
# Create classes and complete logic for make change, total inventory change, reset_all
# error handling
# add total amount of cash in register
# create teller with inventory / maybe just added a CONSTANT that resets when program starts for simplicity.
# create a dict to map over value and quantity
# create a fail safe for empty inventory
# possibly add inventory per register and compare to a total inventory


hundred: Decimal = Decimal("100.00")
fifty: Decimal = Decimal("50.00")
twenty: Decimal = Decimal("20.00")
ten: Decimal = Decimal("10.00")
five: Decimal = Decimal("5.00")
one: Decimal = Decimal("1.00")
quarter: Decimal = Decimal("0.25")
dime: Decimal = Decimal("0.10")
nickel: Decimal = Decimal("0.05")
penny: Decimal = Decimal("0.01")

def make_change() -> Decimal:
    # placeholder for make change
    while True:
        # display menu
        print("\nHow would you like your money split? ")
        print("1. Large Bills")
        print("2. Mixed Bills")
        print("3. Custom Bills")
        print("4. Quit")

        menu_choice: str = input("Enter menu option [1-4]: ")
        menu_choice_int: int = int(menu_choice)

        # print("Splitting money...")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def custom_bills() -> None:
    # placeholder for custom bills logic
    print("Custom Bills...")

def inventory_change() -> None:
    # placeholder for total-inventory-change logic
    print("Tracking inventory change...")

def reset_all() -> None:
    # placeholder for reset logic
    print("Resetting everything...")

def main() -> None:
    print("|-($)-| Welcome to Money Splitter |-($)-|")

    while True:
        # display menu
        print("\n$---- Menu ----$")
        print("1. Split Money")
        print("2. Total Money Split")
        print("3. Reset")
        print("4. Quit")

        choice = input("Enter menu option [1–4]: ").strip()

        # validate that it's an integer, less than 5 and greater than 0
        if not choice.isdigit() or not (1 <= (option := int(choice)) <= 4):
            print("Not a valid input. Please enter a valid menu option.")
            continue

        try:
            match option:
                case 1:
                    make_change()
                case 2:
                    inventory_change()
                case 3:
                    reset_all()
                case 4:
                    print("Goodbye!")
                    break
        except ValueError:
            print("Oops, that didn't seem to work. Please try again.")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# if __name__ == "__main__":
main()
