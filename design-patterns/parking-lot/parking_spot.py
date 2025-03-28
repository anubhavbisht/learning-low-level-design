from vehicle_type import VehicleType
from vehicle import Vehicle

class ParkingSpot:
    def __init__(self, spotNumber: int, parkingSpotType: VehicleType):
        self.spotNumber = spotNumber
        self.parkingType = parkingSpotType
        self.vehicle: Vehicle = None

    def isParkingSpotAvailable(self) -> bool:
        return self.vehicle is None

    def parkVehicle(self, vehicle: Vehicle) -> bool:
        if (
            self.isParkingSpotAvailable()
            and vehicle.getType() == self.parkingType
            and isinstance(vehicle, Vehicle)
        ):
            self.vehicle = vehicle
            return True
        else:
            raise ValueError("Invalid parking type or space not available")

    def unparkVehicle(self) -> Vehicle:
        if self.vehicle is not None:
            vehicle = self.vehicle
            self.vehicle = None
            return vehicle
        else:
            raise ValueError("No vehicle available to unpark")
        
    def getParkingSpotType(self) -> VehicleType:
        return self.parkingType

    def getParkedVehicle(self) -> Vehicle:
        return self.vehicle

    def getSpotNumber(self) -> int:
        return self.spotNumber
