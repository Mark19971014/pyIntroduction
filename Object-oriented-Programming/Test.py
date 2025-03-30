from datetime import date

class MyDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
    
    def get_day(self):
        return self.day
    
    def get_month(self):
        return self.month
    
    def get_year(self):
        return self.year
    
    def set_date(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
    
    def copy(self):
        return MyDate(self.day, self.month, self.year)
    
    @staticmethod
    def now():
        today = date.today()
        return MyDate(today.day, today.month, today.year)

class Tenant:
    def __init__(self, name: str):
        self.name = name
        self.rented_from = None
    
    def get_name(self):
        return self.name
    
    def get_rented_from(self):
        return self.rented_from
    
    def set_rented_from(self, rented_from: MyDate):
        self.rented_from = rented_from

class Residence:
    def __init__(self, number: int, size: float, residence_type: str):
        self._number = number  
        self._size = size      
        self._type = residence_type
        self._rented_to = None    
    
    def get_number(self):
        return self._number

    def set_number(self, new_number: int):
        self._number = new_number

    def is_available(self):
        return self._rented_to is None

    def get_tenant(self):
        return self._rented_to

    def rent_to(self, tenant, rented_from):
        if self.is_available():
            self._rented_to = tenant
            tenant.set_rented_from(rented_from)
    
    def get_number_of_rooms(self):
        raise NotImplementedError("This method should be implemented in subclasses.")

class Room(Residence):
    def __init__(self, number: int, size: float):
        super().__init__(number, size, "Room")
    
    def get_number_of_rooms(self):
        return 1

class Apartment(Residence):
    def __init__(self, number: int, size: float, number_of_rooms: int):
        super().__init__(number, size, "Apartment")
        self.number_of_rooms = number_of_rooms
    
    def get_number_of_rooms(self):
        return self.number_of_rooms

class ApartmentComplex:
    def __init__(self, address: str):
        self.address = address
        self.residences = []
    
    def add_residence(self, residence: Residence):
        self.residences.append(residence)
    
    def get_residence(self, index: int):
        return self.residences[index] if 0 <= index < len(self.residences) else None
    
    def get_residence_by_number(self, number: int):
        for residence in self.residences:
            if residence.get_number() == number:
                return residence
        return None
    
    def get_first_available_room(self):
        for residence in self.residences:
            if isinstance(residence, Room) and residence.is_available():
                return residence
        return None
    
    def get_first_available_apartment(self, min_rooms: int):
        for residence in self.residences:
            if isinstance(residence, Apartment) and residence.is_available() and residence.get_number_of_rooms() >= min_rooms:
                return residence
        return None


# Creating a date object for rental
rental_date = MyDate(15, 3, 2025)

# Creating a tenant
tenant1 = Tenant("John Doe")

# Creating a single room (residence)
room1 = Room(101, 25.5)  # Room number 101 with size 25.5 square meters

# Creating an apartment (residence)
apartment1 = Apartment(201, 75.0, 3)  # Apartment number 201, size 75.0, with 3 rooms

# Creating an apartment complex
apartment_complex = ApartmentComplex("123 Main Street")

# Adding residences to the apartment complex
apartment_complex.add_residence(room1)
apartment_complex.add_residence(apartment1)

# Renting a room to a tenant
if room1.is_available():
    room1.rent_to(tenant1, rental_date)

# Checking if the room is now occupied
print(f"Room 101 is available: {room1.is_available()}")  # Should print False
print(f"Tenant of Room 101: {room1.get_tenant().get_name()}")  # Should print "John Doe"

# Finding the first available room in the apartment complex
available_room = apartment_complex.get_first_available_room()
if available_room:
    print(f"First available room: {available_room.get_number()}")
else:
    print("No available rooms.")

# Finding an available apartment with at least 2 rooms
available_apartment = apartment_complex.get_first_available_apartment(2)
if available_apartment:
    print(f"First available apartment with at least 2 rooms: {available_apartment.get_number()}")
else:
    print("No available apartments with the required number of rooms.")
