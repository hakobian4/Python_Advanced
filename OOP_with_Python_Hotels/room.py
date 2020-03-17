class Room():

    def __init__(self, number, tv = False, refrigerator = False, balcony = False):
        self.number = number
        self.hasTv = tv
        self.hasRefrigerator = refrigerator
        self.hasBalcony = balcony
    
    
    def get_info(self):
        print('\n\t- Room - \nNumber:\t\t{} \nTV:\t\t{} \nRefrigerator:\t{} \nBalcony:\t{}'.format(self.number, self.hasTv, self.hasRefrigerator, self.hasBalcony))