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
# New Customer Rental Workflow
# ----------------------------------------------------

def new_rental(inventory, active_rentals):
    print("--------------------------------------------------")
    print("New Customer Rental")
    print("--------------------------------------------------")

    # Collect rental details
    num_snowboards = get_int("Number of snowboards to rent: ")
    num_skis = get_int("Number of skis to rent: ")

    rental_period = get_nonempty_string("Rental period (Hour/Day/Week): ")
    estimated_length = get_int("Estimated rental length: ")

    coupon = input("Enter coupon code (or press Enter to skip): ").strip()

    # Validate using EquipmentChoice_RentalPeriod
    try:
        EquipmentChoice_RentalPeriod(
            inventory,
            num_snowboards,
            num_skis,
            rental_period,
            estimated_length
        )
    except Exception as e:
        print("Error:", e)
        return

    # Create Rental object
    rental_obj = Rental(inventory, num_snowboards, num_skis, rental_period, estimated_length)

    # Display estimate
    rental_obj.Display_Estimate()

    # Ask customer to confirm
    confirm = input("Complete this rental? (Y/N): ").strip().upper()
    if confirm != "Y":
        print("Rental cancelled.")
        return

    # Collect customer info
    name = get_nonempty_string("Customer name: ")
    id_number = get_int("Customer ID number: ")

    customer = Customer_Information(name, id_number)

    # Remove inventory
    try:
        rental_obj.Remove_From_Inventory()
    except Exception as e:
        print("Error:", e)
        return

    # Store active rental
    active_rentals[id_number] = {
        "customer": customer,
        "rental": rental_obj,
        "snowboards": num_snowboards,
        "skis": num_skis,
        "period": rental_period,
        "estimated_length": estimated_length,
        "coupon": coupon
    }

    print("Rental completed successfully!")


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