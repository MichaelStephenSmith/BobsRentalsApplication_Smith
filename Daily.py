#-----------------------------------------------------
# Class name: Daily
# Class definition: This class inherits rental and
# return. It displays the daily totals.
#-----------------------------------------------------

from Inventory import Inventory
from EquipmentChoice_RentalPeriod import EquipmentChoice_RentalPeriod
from Rental import Rental
from Return import Return


class Daily(Return):

        #-----------------------------------------------------
        # Constructor/Initialization
        #-----------------------------------------------------

        def __init__(self, inventory, intNumSnowBoards, intNumSkis, strHourDayWeek, intLength, intActualLength, strCoupon):
            super().__init__(inventory, intNumSnowBoards, intNumSkis, strHourDayWeek, intLength, intActualLength, strCoupon)

        #-----------------------------------------------------
        # Class Methods
        #-----------------------------------------------------

        def Display_Daily():
            print('------------------Daily Summary-------------------')
            print('Total snowboards rented today: ', Rental.intSBDaily)
            print('Total skis rented today: ', Rental.intSkiDaily)
            print('Total revenue for the day: ', "${:,.2f}".format(Return.dblDailyTotal))






