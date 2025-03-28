from abc import ABC

class CostStrategy(ABC):
    def calculateCost(self, entryTime, exitTime, rate):
        pass

class HourlyCostStrategy(CostStrategy):
    def calculateCost(self, entryTime, exitTime, rate):
        duration = (exitTime - entryTime).seconds // 3600 + 1
        return duration * rate

class MinuteCostStrategy(CostStrategy):
    def calculate_cost(self, entryTime, exitTime, rate):
        duration = (exitTime - entryTime).seconds // 60
        return duration * rate