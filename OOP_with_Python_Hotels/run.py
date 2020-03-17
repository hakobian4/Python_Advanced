from hotel import Hotel
from room import Room
from guest import Guest

def main():
    # Create object of Hotel class
    obj_hotel = Hotel('MARRIOTT', '1 Amiryan Street, Yerevan  0010 Armenia', '+374-10-599000', 'www.marriott.com')

    # Create objects of Guest class
    obj_guest1 = Guest('Armen', 'Hakobian', 'a.sa.92@bk.ru', '091-333-402')   
    obj_guest2 = Guest('Ani', 'Hakobian', 'ani.hakobian.8@gmail.com', '077-587-578')

    # Create objects of Room class
    obj_room1 = Room(1, 'Yes', 'Yes', 'No')   
    obj_room2 = Room(2, 'No', 'Yes', 'Yes')
    obj_room3 = Room(3, 'No', 'Yes', 'No')

    # Add rooms in Hotel
    obj_hotel.add_room(obj_room1)
    obj_hotel.add_room(obj_room2)
    obj_hotel.add_room(obj_room3)
    
    # Book rooms
    obj_hotel.book_room(obj_guest1)
    obj_hotel.book_room(obj_guest2)

    # Print hotel info
    obj_hotel.print_hotel_info()

    # Print all rooms info
    obj_hotel.print_all_rooms()

    # Print room info with a given number (ex. 2)
    obj_hotel.print_room_info(2) 

    # Print guest info
    obj_guest1.get_info()
  
    # Print all booked rooms info
    obj_hotel.print_book_info()
    # or 
    # Print a booked room info by room number 
    obj_hotel.print_book_info(2)


if __name__ == '__main__':
    main() 