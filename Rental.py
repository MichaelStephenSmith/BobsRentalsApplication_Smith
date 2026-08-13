#-----------------------------------------------------
# Class name: Rental
# Class definition: This class calculates the rental 
# cost based on the customers equipment choice and 
# rental period, removes the equipment from the inventory,
# and contains a display method.
#-----------------------------------------------------

from Inventory import Inventory
from EquipmentChoice_RentalPeriod import EquipmentChoice_RentalPeriod

class Rental(EquipmentChoice_RentalPeriod):

        #-----------------------------------------------------
        # Attributes/Class variables
        #-----------------------------------------------------

        intSBDaily = 0
        intSkiDaily = 0

        #-----------------------------------------------------
        # Constructor/Initialization
        #-----------------------------------------------------

        def __init__(self, inventory, intNumSnowBoards, intNumSkis, strHourDayWeek, intLength):
            super().__init__(inventory, intNumSnowBoards, intNumSkis, strHourDayWeek, intLength)

     
        #-----------------------------------------------------
        # Class Methods
        #-----------------------------------------------------

        def Plural(self, strHourDayWeekDisplay):

            if self.strHourDayWeek == 'Hour':
                strHourDayWeekDisplay = 'Hours'
            elif self.strHourDayWeek == 'Day':
                strHourDayWeekDisplay = 'Days'
            else:
                strHourDayWeekDisplay = 'Weeks'

            return strHourDayWeekDisplay

        def calculate(self, intLength):

            if self.strHourDayWeek == 'Hour':

                if self.intLength >= 4:
                    intSBDay = 40
                    intSkiDay = 50
                    dblRentalCost = (self.intNumSnowBoards * intSBDay + self.intNumSkis * intSkiDay)
                else:
                    dblRentalCost = (self.intNumSnowBoards * 10 + self.intNumSkis * 15) * intLength

            elif self.strHourDayWeek == 'Day':

                if self.intLength > 4:
                    intSBWeek = 160
                    intSkiWeek = 200
                    dblRentalCost = (self.intNumSnowBoards * intSBWeek + self.intNumSkis * intSkiWeek)
                else:
                    dblRentalCost = (self.intNumSnowBoards * 40 + self.intNumSkis * 50) * intLength

            else:

                dblRentalCost = (self.intNumSnowBoards * 160 + self.intNumSkis * 200) * intLength

            return dblRentalCost


        def calculate_rental_cost(self):

            return self.calculate(self.intLength)


        def Display_Estimate(self):

            if self.intLength > 1:
                strHourDayWeekDisplay = self.Plural(self.strHourDayWeek)
            else:
                strHourDayWeekDisplay = self.strHourDayWeek

            print('-----------------Rental Estimate------------------')
            print('Number of snowboards rented: ', self.intNumSnowBoards)
            print('Number of skis rented: ', self.intNumSkis)
            print('Rental period: ', self.intLength, strHourDayWeekDisplay)
            print('Total rental cost:' , "${:,.2f}".format(self.calculate_rental_cost()))


        def Remove_From_Inventory(self):

            if self.intNumSnowBoards > self.inventory.intSnowboardInventory:
                raise Exception(f'There is only', self.inventory.intSnowboardInventory, 'snowboards in stock.')

            if self.intNumSkis > self.inventory.intSkiInventory:
                raise Exception(f'There is only', self.inventory.intSkiInventory, 'skis in stock.')

            self.inventory.intSnowboardInventory -= self.intNumSnowBoards
            self.inventory.intSkiInventory -= self.intNumSkis

            Rental.intSBDaily += self.intNumSnowBoards
            Rental.intSkiDaily += self.intNumSkis