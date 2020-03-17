from room import Room
from guest import Guest

class Hotel():
    
    def __init__(self, name, address, phone, web):
        self.name = name
        self.address = address
        self.phone = phone
        self.web = web
        self.free_room_numbers = []
        self.busy_rooms = []
        self.all_rooms = []
        
    def add_room(self, obj_room):
        """
            This method adds rooms to hotel.
        """
        does_room_exist = False
        for i in range(len(self.all_rooms)):
            if self.all_rooms[i].number == obj_room.number:
                does_room_exist = True
                break
            else: 
                pass
        if does_room_exist == False:
            self.all_rooms.append(obj_room)
            self.free_room_numbers.append(obj_room.number)
        else:
            print('This hotel already has current room with number {}'.format(obj_room.number))


    def book_room(self, obj_guest):
        """
            This method allows book rooms.
        """
        if len(self.free_room_numbers) != 0:
            d = {'number' : self.free_room_numbers[0], 'guest' : obj_guest}
            self.busy_rooms.append(d)
            print('You have booked the room with number ', self.free_room_numbers[0])
            self.free_room_numbers.remove(self.free_room_numbers[0])
        else:
            print('You have not free rooms')


    def print_room_info(self, room_number):
        """
            This metod prints the room info, based on room number.

        """
        does_room_exist = False
        for i in range(len(self.all_rooms)):
            if self.all_rooms[i].number == room_number:
                does_room_exist = True
                break
            else: 
                pass
        if does_room_exist:
            self.all_rooms[i].get_info()
        else:
            print('In this hotel there is no room with number {}'.format(room_number))


    def print_all_rooms(self):
        """
            This method prints info about all the rooms in the hotel.
        """
        for room in self.all_rooms:
            room.get_info()


    def print_book_info(self, room_number = None):
        """
            This method prints info about all the booked rooms.
        """
        if room_number is None:
            for room in self.busy_rooms:
                room['guest'].get_info()
                print('Room Number:\t{}'.format(room['number']))
        else:
            exists_in_busy = False
            for room in self.busy_rooms:
                if room['number'] == room_number:
                    exists_in_busy = True
                    break
                else:
                    pass
            if  exists_in_busy:
                room['guest'].get_info()
                print('Room Number:\t{}'.format(room['number']))
            else:
                print('The room is not booked yet. You can book it.')


    def print_hotel_info(self):
        print('\n --> HOTEL {} <-- \nAddress:\t{} \nRoom Count:\t{} \nTelephone:\t{} \nWEB Address:\t{}'.format(self.name, self.address, len(self.all_rooms), self.phone, self.web))