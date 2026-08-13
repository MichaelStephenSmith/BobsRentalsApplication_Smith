#-----------------------------------------------------
# Class name: Inventory
# Class definition: This class gathers and stores 
# inventory of snowboards and skis and contains a 
# display method
#-----------------------------------------------------

class Inventory:

        #-----------------------------------------------------
        # Constructor/Initialization
        #-----------------------------------------------------

        def __init__(self, intSnowboardInventory = 0, intSkiInventory = 0):
            self.intSnowboardInventory = intSnowboardInventory
            self.intSkiInventory = intSkiInventory


        #-----------------------------------------------------
        # Getters
        #-----------------------------------------------------

        @property
        def intSnowboardInventory(self):
            return self._intSnowboardInventory

        @property
        def intSkiInventory(self):
            return self._intSkiInventory



        #-----------------------------------------------------
        # Setters
        #-----------------------------------------------------

        @intSnowboardInventory.setter
        def intSnowboardInventory(self, intSnowboardInventory):
            if intSnowboardInventory < 0:
                raise Exception('intSnowboardInventory must be 0 or greater.')
            else:
                self._intSnowboardInventory = intSnowboardInventory

        @intSkiInventory.setter
        def intSkiInventory(self, intSkiInventory):
            if intSkiInventory < 0:
                raise Exception('intSkiInventory must be 0 or greater.')
            else:
                self._intSkiInventory = intSkiInventory


         #-----------------------------------------------------
         # Class Methods
         #-----------------------------------------------------

        def Show_Inventory(self):

            print('-------------------Inventory----------------------')
            print('Number of snowboards availible: ', self.intSnowboardInventory)
            print('Number of skis availible: ', self.intSkiInventory)




