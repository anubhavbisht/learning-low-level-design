from vehicle_type import VehicleType
from vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self, licence: str):
        super().__init__(licence, VehicleType.BIKE)
