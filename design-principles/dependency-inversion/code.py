from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PayPalPaymentProcessor(PaymentProcessor):
    def pay(self, amount):
        return f"Paid {amount} via PayPal"


class StripePaymentProcessor(PaymentProcessor):
    def pay(self, amount):
        return f"Paid {amount} via Stripe"


class OrderService:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def checkout(self, amount):
        return self.payment_processor.pay(amount)


paypal_processor = PayPalPaymentProcessor()
stripe_processor = StripePaymentProcessor()

order1 = OrderService(paypal_processor)
order2 = OrderService(stripe_processor)

print(order1.checkout(100)) 
print(order2.checkout(200))