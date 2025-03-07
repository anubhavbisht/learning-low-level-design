from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass


class PaypalPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid amount via paypal", amount)


class StripePayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid amount via stripe", amount)


class PaymentProcessor:
    def __init__(self, paymentStrategy: PaymentStrategy):
        self.paymentStrategy = paymentStrategy
        
    def processPayment(self, amount):
        self.paymentStrategy.pay(amount)
        
paypal = PaymentProcessor(PaypalPayment())
stripe = PaymentProcessor(StripePayment())

paypal.processPayment(100)
stripe.processPayment(100)