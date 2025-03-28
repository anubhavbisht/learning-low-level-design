from abc import ABC
from vehicle_type import VehicleType

class Vehicle(ABC):
    def __init__(self, vehicleNo: str, vehicle_type: VehicleType):
        self.vehicleNo = vehicleNo
        self.type = vehicle_type

    def getType(self) -> VehicleType:
        return self.type
    
    def getVehicleId(self) -> str:
        return self.vehicleNo
