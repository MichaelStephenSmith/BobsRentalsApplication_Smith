#----------------------------------------------------
# Katrina Moore
# Final, Part 1
#----------------------------------------------------


from Inventory import Inventory
from EquipmentChoice_RentalPeriod import EquipmentChoice_RentalPeriod
from Rental import Rental
from Return import Return
from Daily import Daily



def Main():

    print('--------------------------------------------------')
    print('Inventory')
    print('--------------------------------------------------')

    inventory = Inventory(25, 19)
    inventory.Show_Inventory()
    print('')
    print('')

    print('--------------------------------------------------')
    print('Rental/Return #1')
    print('--------------------------------------------------')

    R1 = Rental(inventory, 2, 3, 'Day', 5)
    R1.Display_Estimate()
    R1.Remove_From_Inventory()
    inventory.Show_Inventory()
    Return1 = Return(inventory, 2, 3, 'Day', 5, 6, '448BBP')
    Return1.Display_Actual_Cost()
    Return1.Add_To_Inventory()
    inventory.Show_Inventory()
    print('')
    print('')

    print('--------------------------------------------------')
    print('Rental/Return #2')
    print('--------------------------------------------------')

    R2 = Rental(inventory, 1, 1, 'Hour', 2)
    R2.Display_Estimate()
    R2.Remove_From_Inventory()
    inventory.Show_Inventory()
    Return2= Return(inventory, 1, 1, 'Hour', 2, 3, 'ggtSzZ')
    Return2.Display_Actual_Cost()
    Return2.Add_To_Inventory()
    inventory.Show_Inventory()
    print('')
    print('')

    print('--------------------------------------------------')
    print('Daily Totals')
    print('--------------------------------------------------')

    Daily.Display_Daily()



Main()





