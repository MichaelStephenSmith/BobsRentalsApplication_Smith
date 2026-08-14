# BobsRentalsApplication_Smith
Final Part 2: Application Development

Michael Smith
Object-Orient Programming CPDM 120-400

# PROJECT SUMMARY
This project implements a complete console?based Python application for Bob’s Ski & Snowboard Rentals. The goal was to build a fully functional
rental system using a class library created by another student. The application manages starting inventory, processes new rentals, handles returns,
applies discounts, tracks active rentals, and displays end?of?day totals. All business logic pricing, discounts, inventory changes, and daily totals
is handled by the assigned classes, while the application controls menus, input validation, customer information, and rental tracking.

# HOW TO USE THE PROGRAM
Place all the provided class files and main.py in the same folder. Open a terminal, navigate to that folder, and run the program using: python main.py
Follow the on?screen menu to enter starting inventory, create rentals, process returns, view inventory, and end the day. The program will exit automatically
after selecting End of Day.

# USE OF ASSIGNED CLASSES
I used the assigned class library exactly as provided, without modifying any of the original files. Each class was integrated into the application
according to its intended purpose:

Inventory stores and displays available skis and snowboards. Inventory changes only through Rental.Remove_From_Inventory() and Return.Add_To_Inventory().

EquipmentChoice_RentalPeriod validates rental requests, including quantities, rental period, and rental length. This class ensures all rental
input is valid before a Rental object is created.

Rental calculates estimated rental cost using the best available price and updates daily totals for equipment rented. The application calls
Display_Estimate() before confirming a rental.

Return calculates actual rental cost, applies family and coupon discounts, restores inventory, and updates daily revenue totals. The application
uses Display_Actual_Cost() to show the final invoice.

Daily prints end of day totals using class variables stored in Rental and Return.

Customer_Information stores customer name and ID and is attached to each active rental record.

The application wraps around these classes to provide menus, input validation, rental tracking, and program flow, while leaving all business logic
inside the original class library.

# PROBLEMS AND LIMITATIONS
I ran into a few problems and limitations when creating the additional code.

The Daily class does not calculate totals, it only prints values stored in other classes.

The Rental class does not store customer information, coupon codes, or rental length, so the application maintains an active_rentals dictionary.

The Return class only checks whether a coupon ends with “BBP,” so the application handles blank or missing coupon input.

The class library does not track active rentals or timestamps, so the application collects rental length manually.

The classes use exceptions for validation, so the application wraps class calls in try/except blocks.

Limitations were expected and documented, and the application was designed to work effectively within the constraints of the provided class library.

# REFLECTION
Working with another programmer’s code was a realistic and valuable experience. It required me to read and understand unfamiliar class structures,
identify how each class was intended to function, and design my application around those constraints. Instead of rewriting or modifying the original
class files, I had to adapt my workflow to fit the existing design, fill in missing features at the application level, and document limitations clearly.
This project strengthened my ability to integrate external code, troubleshoot design gaps, and build clean, maintainable application logic on top of
someone else’s work—skills that are essential in real world software development.
