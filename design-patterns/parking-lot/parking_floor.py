from parking_spot import ParkingSpot
from typing import List
from vehicle_type import VehicleType


class ParkingFloor:
    def __init__(self, floorNumber: int, numberOfSpots: int, config=None):
        self.floorNumber = floorNumber
        self.parkingSpots: List[ParkingSpot] = []
        self.initializeFloor(numberOfSpots, config)
        
    def getFloorNumber(self) -> int:
        return self.floorNumber

    def initializeFloor(self, numberOfSpots: int, config):
        if config:
            totalPercentage = sum(config.values())
            if totalPercentage > 1:
                raise ValueError("Configuation is not correct")
            slotDistribution = {
                vt: int(numberOfSpots * pct) for vt, pct in config.items()
            }
        else:
            defaultDistribution = {
                VehicleType.CAR: 0.5,
                VehicleType.BIKE: 0.3,
                VehicleType.TRUCK: 0.2,
            }
            slotDistribution = {
                vt: int(numberOfSpots * pct) for vt, pct in defaultDistribution.items()
            }
        totalAssigned = sum(slotDistribution.values())
        remainingSpots = numberOfSpots - totalAssigned
        if remainingSpots > 0:
            defaultVehicleType = list(slotDistribution.keys())[0]
            slotDistribution[defaultVehicleType] += remainingSpots

        for vt, count in slotDistribution.items():
            for _ in range(count):
                self.parkingSpots.append(ParkingSpot(len(self.parkingSpots) + 1, vt))

    def addParkingSpot(self, vehicleType: VehicleType):
        newSpotNumber = len(self.parkingSpots) + 1
        self.parkingSpots.append(ParkingSpot(newSpotNumber), vehicleType)
    
    def addMultipleParkingSpots(self, numSpots: int, vehicleType: VehicleType):
        for _ in range(numSpots):
            self.addParkingSpot(vehicleType)
    
    def findAvailableSpot(self, vehicleType: VehicleType) -> ParkingSpot:
        for spot in self.parkingSpots:
            if spot.isParkingSpotAvailable() and spot.getParkingSpotType() == vehicleType:
                return ParkingSpot
        return None
    
    def availablityStatus(self):
        occupiedSpots = sum(1 for spot in self.parkingSpots if spot.isParkingSpotAvailable())
        totalSpots = len(self.parkingSpots)
        return {
            "floorNumber": self.floorNumber,
            "totalSpots": totalSpots,
            "occupiedSpots": occupiedSpots,
            "freeSpots": totalSpots - occupiedSpots,
            "vehiclesParked": {vt.value: sum(1 for spot in self.parkingSpots if spot.isParkingSpotAvailable() and spot.getParkingSpotType() == vt) for vt in VehicleType}
        }