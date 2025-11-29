TRAIN_DATA = {
    1224: {'name': 'Shatabdi Express', 'dep': 'Ahmedabad', 'arr': 'Surat', 'price': 2100, 'seats': 72},
    5569: {'name': 'Rajdhani Express', 'dep': 'Ratlam', 'arr': 'Mumbai', 'price': 4500, 'seats': 100},
    7741: {'name': 'Vande Bharat Express', 'dep': 'Ratlam', 'arr': 'Pune', 'price': 4200, 'seats': 52},
    9462: {'name': 'Ratlam Express', 'dep': 'Udaipur', 'arr': 'Indore', 'price': 1200, 'seats': 50},
    8106: {'name': 'Hindustan Express', 'dep': 'Mumbai', 'arr': 'Chennai', 'price': 8500, 'seats': 175},
    8462: {'name': 'IND-National Express', 'dep': 'Delhi', 'arr': 'Chennai', 'price': 12500, 'seats': 39},
    7410: {'name': 'Kolkata Express', 'dep': 'Kolkata', 'arr': 'Hyderabad', 'price': 8750, 'seats': 69},
    9630: {'name': 'North-IND-Express', 'dep': 'Shimla', 'arr': 'Jaipur', 'price': 1500, 'seats': 89},
    8562: {'name': 'Kalka Mali Express', 'dep': 'Panjab', 'arr': 'Chandigarh', 'price': 1700, 'seats': 150},
    9510: {'name': 'Chennai-Jaipur-Express', 'dep': 'Jaipur', 'arr': 'Delhi', 'price': 750, 'seats': 62},
    7531: {'name': 'Purna-Hyderabad P-E', 'dep': 'Mumbai', 'arr': 'Pune', 'price': 1500, 'seats': 126},
    6249: {'name': 'Howrah-Mumbai Mali', 'dep': 'Bangalore', 'arr': 'Thane', 'price': 1200, 'seats': 98},
    8176: {'name': 'Duronto Express', 'dep': 'Ratlam', 'arr': 'Kashmir', 'price': 9500, 'seats': 70},
    4371: {'name': 'Humsafar Express', 'dep': 'Udaipur', 'arr': 'Ahmedabad', 'price': 1000, 'seats': 129},
    9865: {'name': 'Island Express', 'dep': 'Haryana', 'arr': 'Lucknow', 'price': 2750, 'seats': 129}
}
class Train:
    def __init__(self, number, name, dep, arr, price, max_seats):
        self.number = number
        self.name = name
        self.departure = dep
        self.arrival = arr
        self.price = price
        self.max_seats = max_seats

        # We set the derived attributes INTERNALLY
        self.booked_seats = 0
        self.available_tickets = max_seats

    def __str__(self):
        return f"Train {self.number} ({self.name}): {self.departure} -> {self.arrival}"
class RailBoard:
    def __init__(self):
        self.all_trains = {}
        for train_num, details in TRAIN_DATA.items():
            new_train = Train(
                train_num,
                details['name'],
                details['dep'],
                details['arr'],
                details['price'],
                details['seats']
            )
            self.all_trains[train_num] = new_train
        print(f"Loaded {len(self.all_trains)} trains successfully.")

    def book_ticket(self, train_number, num_tickets):
        if train_number not in self.all_trains:
            print("Error: Invalid Train Number.")
            return False

        train = self.all_trains[train_number]

        if train.available_tickets >= num_tickets:
            train.available_tickets -= num_tickets
            train.booked_seats += num_tickets
            total_price = num_tickets * train.price

            print(f"\n✅ BOOKING CONFIRMED for Train {train.number} ({train.name})")
            print(f"   Tickets: {num_tickets} | Total Price: ₹{total_price}")
            print(f"   Remaining Seats: {train.available_tickets}")
            return True
        else:
            print(f"❌ Cannot book {num_tickets} tickets.")
            print(f"   Only {train.available_tickets} seats remaining.")
            return False


rail_board = RailBoard()

print("\n--- TEST 1: SUCCESSFUL BOOKING ---")
rail_board.book_ticket('1224', 1)

print("\n--- TEST 2: FAILED BOOKING (OVER CAPACITY) ---")
rail_board.book_ticket('1224', 75)

print("\n--- TEST 3: SUCCESSFUL BOOKING ---")
rail_board.book_ticket('5569', 5)

print(f"\n--- CURRENT STATUS CHECK ---")
print(f"Train 1224 Remaining Seats: {rail_board.all_trains[1224].available_tickets}")
print(f"Train 5569 Booked Seats: {rail_board.all_trains[5569].booked_seats}")