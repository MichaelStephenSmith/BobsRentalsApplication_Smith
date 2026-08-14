# ----------------------------------------------------
# Bob’s Ski & Snowboard Rentals - Application (Part 2)
# ----------------------------------------------------

from Inventory import Inventory
from EquipmentChoice_RentalPeriod import EquipmentChoice_RentalPeriod
from Rental import Rental
from Return import Return
from Daily import Daily
from Customer_Information import Customer_Information

# ----------------------------------------------------
# Helper Functions
# ----------------------------------------------------

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Invalid input. Please enter a whole number.")

def get_nonempty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be blank.")

# ----------------------------------------------------
# Application Startup
# ----------------------------------------------------

def startup_inventory():
    print("Welcome to Bob’s Ski & Snowboard Rentals!")
    print("Enter starting inventory.")

    while True:
        try:
            snowboards = get_int("Enter number of snowboards: ")
            skis = get_int("Enter number of skis: ")
            inventory = Inventory(snowboards, skis)
            return inventory
        except Exception as e:
            print("Error:", e)
            print("Please try again.")

# ----------------------------------------------------
# Main Menu Loop
# ----------------------------------------------------

def main():
    inventory = startup_inventory()
    active_rentals = {}

    while True:
        print("--------------------------------------------------")
        print("Main Menu")
        print("--------------------------------------------------")
        print("1. New Customer Rental")
        print("2. Rental Return")
        print("3. Show Inventory")
        print("4. End of Day")

        choice = get_nonempty_string("Select an option: ")

        if choice == "1":
            new_rental(inventory, active_rentals)
        elif choice == "2":
            rental_return(inventory, active_rentals)
        elif choice == "3":
            show_inventory(inventory)
        elif choice == "4":
            end_of_day()
        else:
            print("Invalid selection. Please try again.")

main()