from abc import ABC

class PaymentStrategy(ABC):
    def processPayment(self, amount):
        pass

class CashPayment(PaymentStrategy):
    def processPayment(self, amount):
        return f"Paid {amount} in cash."

class CardPayment(PaymentStrategy):
    def processPayment(self, amount):
        return f"Paid {amount} via card."