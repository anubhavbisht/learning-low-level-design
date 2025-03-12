from abc import ABC, abstractmethod

class BasePizza(ABC):
    @abstractmethod
    def cost(self):
        pass

class PlainPizza(BasePizza):
    def cost(self):
        return 100

class CheesePizza(BasePizza):
    def cost(self):
        return 150

class MarghareitaPizza(BasePizza):
    def cost(self):
        return 200

class ToppingsDecorator(BasePizza): 
    @abstractmethod
    def cost(self):
        pass

class MushroomPizza(ToppingsDecorator):
    def __init__(self, basePizza: BasePizza):
        self.basePizza = basePizza
    
    def cost(self):
        return self.basePizza.cost() + 20

class OnionPizza(ToppingsDecorator):
    def __init__(self, basePizza: BasePizza):
        self.basePizza = basePizza
    
    def cost(self):
        return self.basePizza.cost() + 30

class TomatoPizza(ToppingsDecorator):
    def __init__(self, basePizza: BasePizza):
        self.basePizza = basePizza
    
    def cost(self):
        return self.basePizza.cost() + 40

pizza = MarghareitaPizza()  
print(pizza.cost())  

pizza_with_mushroom = MushroomPizza(pizza)
print(pizza_with_mushroom.cost())  

pizza_with_onion_tomato = TomatoPizza(OnionPizza(pizza))
print(pizza_with_onion_tomato.cost())  