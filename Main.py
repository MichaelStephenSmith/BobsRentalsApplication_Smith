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

def main():
    print("Bob’s Ski & Snowboard Rentals")
main()