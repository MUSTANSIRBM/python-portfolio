class Car:
    def __init__(self,number_plate,name):
        self.number_plate = number_plate
        self.name = name
    def __str__(self):
        return f'{self.name} - {self.number_plate}'
class Parking_Lot:
    def __init__(self):
        self.cars = []
        self.capacity = 5
    def park_car(self, number_plate, name):
        if len(self.cars) < self.capacity:
            new_car = Car(number_plate, name)
            self.cars.append(new_car)
            spot = len(self.cars)
            print(f"✅ Success! {new_car.name} is parked in spot **#{spot}**.")
        else:
            print("Sorry, lot is full. No spots available.")
    def unpark_car(self,plate_remove):
        found_car = None

        for car in self.cars:
            if car.number_plate == plate_remove:
                found_car = car
                break
        if found_car:
            self.cars.remove(found_car)
            print(f'Car {found_car.number_plate} (Model: {found_car.name}) has been successfully unparked.')
        else:
            print(f"Error: Car with plate {plate_remove} not found in the lot.")

    def view_parked_cars(self):  # Renamed for clarity
        print(f"\n--- 🅿️ Parking Lot Status ({len(self.cars)}/{self.capacity}) ---")
        if not self.cars:
            print("The lot is empty.")
        else:
            # We use enumerate to show the spot number (index + 1)
            for index, car in enumerate(self.cars):
                print(f"Spot #{index + 1}: {car}")
        print("---------------------------------------")





# Assuming you implemented the fixed Car and Lot classes above
my_lot = Parking_Lot()

# --- Parking Test ---
print("--- Parking Cars ---")
my_lot.park_car("MH12-1111", "Audi A4")
my_lot.park_car("DL01-2222", "Honda Civic")
my_lot.park_car("KA03-3333", "Maruti Swift")
my_lot.park_car("TN04-4444", "Tata Nexon")
my_lot.park_car("GJ05-5555", "Toyota Camry")

# --- Check Full Lot ---
my_lot.park_car("RJ06-6666", "BMW X5") # Should print "Sorry, lot is full."

# --- View Status ---
my_lot.view_parked_cars()

# --- Unparking Test ---
print("\n--- Unparking Cars ---")
my_lot.unpark_car("DL01-2222") # Success
my_lot.unpark_car("RJ06-6666") # Error (Not found)

# --- View Status After Unpark ---
my_lot.view_parked_cars()

# --- Parking in the free spot ---
my_lot.park_car("MP07-7777", "New Mini Cooper") # Should succeed
my_lot.view_parked_cars()