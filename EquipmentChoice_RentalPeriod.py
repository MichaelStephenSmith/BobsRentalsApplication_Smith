#-----------------------------------------------------
# Class name: EquipmentChoice_RentalPeriod
# Class definition: This class gathers the customers 
# equipment choice and rental period, then checks to make 
# sure the input is valid.
#-----------------------------------------------------
from Inventory import Inventory

class EquipmentChoice_RentalPeriod:

        #-----------------------------------------------------
        # Constructor/Initialization
        #-----------------------------------------------------

        def __init__(self, inventory, intNumSnowBoards, intNumSkis, strHourDayWeek, intLength):

            self.inventory = inventory
            self.intNumSnowBoards = intNumSnowBoards
            self.intNumSkis = intNumSkis
            self.strHourDayWeek = strHourDayWeek
            self.intLength = intLength

            if intNumSkis == 0 and self.intNumSnowBoards == 0:
                raise Exception('Rental must include least one snowboard or ski.')
        #-----------------------------------------------------
        # Getters
        #-----------------------------------------------------

        @property
        def intNumSnowBoards(self):
            return self._intNumSnowBoards

        @property
        def intNumSkis(self):
            return self._intNumSkis

        @property
        def strHourDayWeek(self):
            return self._strHourDayWeek

        @property
        def intLength(self):
            return self._intLength



        #-----------------------------------------------------
        # Setters
        #-----------------------------------------------------

        @intNumSnowBoards.setter
        def intNumSnowBoards(self, intNumSnowboards):

            if intNumSnowboards < 0:
                raise Exception('intNumSnowboards must be 0 or greater.')
            elif intNumSnowboards > self.inventory.intSnowboardInventory:
                raise Exception(f'There is only', self.inventory.intSnowboardInventory, 'snowboards in stock.')
            else:
                self._intNumSnowBoards = intNumSnowboards


        @intNumSkis.setter
        def intNumSkis(self, intNumSkis):
             if intNumSkis < 0:
                raise Exception('intNumSkis must be 0 or greater.')
             elif intNumSkis > self.inventory.intSkiInventory:
                raise Exception(f'There is only', self.inventory.intSkiInventory, 'skis in stock.')
             else:
                self._intNumSkis = intNumSkis


        @strHourDayWeek.setter
        def strHourDayWeek(self, strHourDayWeek):
            if strHourDayWeek not in ['Hour', 'Day', 'Week']:
                raise Exception('strHourDayWeek must be "Hour", "Day", or "Week".')
            else:
                self._strHourDayWeek = strHourDayWeek


        @intLength.setter
        def intLength(self, intLength):
            if intLength <= 0:
                raise Exception('intLength must be greater than 0.')
            else:
                self._intLength = intLength