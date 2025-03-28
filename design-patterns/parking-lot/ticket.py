import uuid
from datetime import datetime
from parking_floor import ParkingFloor
from parking_spot import ParkingSpot
from vehicle import Vehicle


class Ticket:
    def __init__(self, floor: ParkingFloor, vehicle: Vehicle, spot: ParkingSpot):
        self.ticketId = str(uuid.uuid4())
        self.floor = floor
        self.parkingSpot = spot
        self.vehicle = vehicle
        self.entryTime = datetime.now()
