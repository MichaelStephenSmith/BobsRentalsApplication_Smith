#-----------------------------------------------------
# Class name: Return
# Class definition: This class calculates the rental 
# cost based on the actual length of time the customer 
# had the equipment, adds the equipment back to the 
# inventory, and contains a display method.
#-----------------------------------------------------

from Inventory import Inventory
from EquipmentChoice_RentalPeriod import EquipmentChoice_RentalPeriod
from Rental import Rental
   

class Return(Rental):

        #-----------------------------------------------------
        # Attributes/Class variables
        #-----------------------------------------------------

        dblDailyTotal = 0

        #-----------------------------------------------------
        # Constructor/Initialization
        #-----------------------------------------------------

        def __init__(self, inventory, intNumSnowBoards, intNumSkis, strHourDayWeek, intLength, intActualLength, strCoupon):
            super().__init__(inventory, intNumSnowBoards, intNumSkis, strHourDayWeek, intLength)
    
            self.intActualLength = intActualLength
            self.strCoupon = strCoupon

        #-----------------------------------------------------
        # Getters
        #-----------------------------------------------------

        @property
        def intActualLength(self):
            return self._intActualLength

        #-----------------------------------------------------
        # Setters
        #-----------------------------------------------------

        @intActualLength.setter
        def intActualLength(self, intActualLength):
            if intActualLength <= 0:
                raise Exception('intActualLength must be greater than 0.')
            else:
                self._intActualLength = intActualLength


        #-----------------------------------------------------
        # Class Methods
        #-----------------------------------------------------


        def calculate_actual_rental_cost(self):

            return self.calculate(self.intActualLength)
        

        def Determine_Discounts(self, dblBeforeDiscount):

            dblAfterDiscount = dblBeforeDiscount

            if self.intNumSkis + self.intNumSnowBoards in range (3,6):
                dblAfterDiscount = dblAfterDiscount - (dblAfterDiscount * .25)

            if self.strCoupon.endswith('BBP'):
                dblAfterDiscount = dblAfterDiscount - (dblAfterDiscount * .1)

            return dblAfterDiscount


        def Display_Actual_Cost(self):

            if self.intLength > 1:
                strHourDayWeekDisplay = self.Plural(self.strHourDayWeek)
            else:
                strHourDayWeekDisplay = self.strHourDayWeek

            dblBeforeDiscount = self.calculate_actual_rental_cost()

            dblAfterDiscount = self.Determine_Discounts(dblBeforeDiscount)

            Return.dblDailyTotal += dblAfterDiscount

            print('---------------Rental Actual Cost-----------------')
            print('Number of snowboards rented: ', self.intNumSnowBoards)
            print('Number of skis rented: ', self.intNumSkis)
            print('Rental period: ', self.intActualLength, strHourDayWeekDisplay)
            print('Total rental cost:' , "${:,.2f}".format(dblAfterDiscount))
        
        def Add_To_Inventory(self):

            self.inventory.intSnowboardInventory += self.intNumSnowBoards
            self.inventory.intSkiInventory += self.intNumSkis