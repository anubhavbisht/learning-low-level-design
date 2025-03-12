class Discount:
    def get_discount(self, customer_type, price):
        if customer_type == "regular":
            return price * 0.9  
        elif customer_type == "vip":
            return price * 0.8  
        else:
            return price  

from abc import ABC, abstractmethod

class NewDiscount(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class RegularDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.9  

class VIPDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.8  

class SuperVIPDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.7  

def calculate_discount(price, discount_strategy: Discount):
    return discount_strategy.apply_discount(price)

regular = RegularDiscount()
vip = VIPDiscount()
super_vip = SuperVIPDiscount()

print(calculate_discount(100, regular))  
print(calculate_discount(100, vip))  
print(calculate_discount(100, super_vip))  

