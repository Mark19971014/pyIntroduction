from datetime import date
from typing import List, Optional


class MyDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self) -> int:
        return self.day

    def get_month(self) -> int:
        return self.month

    def get_year(self) -> int:
        return self.year

    def set(self, day: int, month: int, year: int):
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
        self.rented_from: Optional[MyDate] = None

    def get_name(self) -> str:
        return self.name

    def get_rented_from(self) -> Optional[MyDate]:
        return self.rented_from

    def set_rented_from(self, date: MyDate):
        self.rented_from = date


class Residence:
    def __init__(self, number: int, size: float, residence_type: str):
        self.number = number
        self.size = size
        self.type = residence_type
        self.tenant: Optional[Tenant] = None

    def get_number(self) -> int:
        return self.number

    def get_size(self) -> float:
        return self.size

    def get_type(self) -> str:
        return self.type

    def is_available(self) -> bool:
        return self.tenant is None

    def rent_to(self, tenant: Tenant, rented_from: MyDate):
        if self.is_available():
            self.tenant = tenant
            tenant.set_rented_from(rented_from)
        else:
            raise Exception("Residence is already occupied")

    def get_tenant(self) -> Optional[Tenant]:
        return self.tenant

    def get_number_of_rooms(self) -> int:
        raise NotImplementedError("This method should be implemented in subclasses")


class Room(Residence):
    def __init__(self, number: int, size: float):
        super().__init__(number, size, "Room")

    def get_number_of_rooms(self) -> int:
        return 1


class Apartment(Residence):
    def __init__(self, number: int, size: float, number_of_rooms: int):
        super().__init__(number, size, "Apartment")
        self.number_of_rooms = number_of_rooms

    def get_number_of_rooms(self) -> int:
        return self.number_of_rooms


class ApartmentComplex:
    def __init__(self, address: str):
        self.address = address
        self.residences: List[Residence] = []

    def get_number_of_residences(self) -> int:
        return len(self.residences)

    def add(self, residence: Residence):
        self.residences.append(residence)

    def get_residence(self, index: int) -> Residence:
        if 0 <= index < len(self.residences):
            return self.residences[index]
        else:
            raise IndexError("Invalid index")

    def get_residence_by_number(self, number: int) -> Optional[Residence]:
        for residence in self.residences:
            if residence.get_number() == number:
                return residence
        return None

    def get_first_available_room(self) -> Optional[Room]:
        for residence in self.residences:
            if isinstance(residence, Room) and residence.is_available():
                return residence
        return None

    def get_first_available_apartment(self, min_no_of_rooms: int) -> Optional[Apartment]:
        for residence in self.residences:
            if isinstance(residence, Apartment) and residence.is_available() and residence.get_number_of_rooms() >= min_no_of_rooms:
                return residence
        return None
