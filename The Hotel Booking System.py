class Room:
    def __init__(self,room_number,price,room_type):
        self.room_number = room_number
        self.price  = price
        self.type = room_type
        self.is_booked = False
    def __str__(self):
        status =  "Occupied" if self.is_booked else "Available"
        return f"[{self.room_number}] - ${self.price} ({status})"
class Hotel:
    def __init__(self):
        self.rooms =[]
        self.load_data()
    def add_room(self,room_number,price,type):
        h = Room(room_number, price, type)
        self.rooms.append(h)
        self.save_data()
    def book_room(self,room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_booked:
                    print("Already occupied!")
            else:
                room.is_booked = True
                print("Booking Confirmed!")
                self.save_data()
            return  # Stop looking after finding the room
        print("Room not found.")

    def checkout(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                room.is_booked = False
                print("Checked out")
                self.save_data()
                return
        print("Room not found.")
    def show_available(self):
        for r in self.rooms:
            if not r.is_booked:
                print(f'{r}')
            return
    def save_data(self):
        with open('Hotel.txt' , 'w') as f:
            for line in self.rooms:
                f.write(f'{line.room_number} {line.price} {line.type} {line.is_booked}\n')

    def load_data(self):
        self.rooms = []
        try:
            with open('Hotel.txt', 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line: continue

                    parts = line.split(',')

                    # SAFETY CHECK: Ensure we have exactly 4 parts before unpacking
                    if len(parts) != 4:
                        print(f"Skipping corrupt or old format line: {line}")
                        continue

                    # 1. Read string data
                    r_num, price, r_type, is_booked_str = parts

                    # 2. Recreate Object
                    loaded_room = Room(r_num, int(price), r_type)

                    # 3. CRITICAL: Convert string "True" back to boolean True
                    loaded_room.is_booked = (is_booked_str == 'True')

                    self.rooms.append(loaded_room)
        except FileNotFoundError:
            # First run behavior
            pass

hilton = Hotel()
hilton.add_room("101", 100, "Single")
hilton.add_room("102", 200, "Double")

hilton.book_room("101") # Success
hilton.book_room("101") # Fail (Occupied)

hilton.show_available() # Should only show 102

hilton.checkout("101")
hilton.show_available() # Should show 101 and 102


