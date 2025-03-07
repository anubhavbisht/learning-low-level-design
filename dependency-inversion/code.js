class PaymentProcessor {
  pay(amount) {
    throw new Error("Method must be implemented");
  }
}

class PayPalPaymentProcessor extends PaymentProcessor {
  pay(amount) {
    return `Paid ${amount} via PayPal`;
  }
}

class StripePaymentProcessor extends PaymentProcessor {
  pay(amount) {
    return `Paid ${amount} via Stripe`;
  }
}

class OrderService {
  constructor(paymentProcessor) {
    this.paymentProcessor = paymentProcessor;
  }

  checkout(amount) {
    return this.paymentProcessor.pay(amount);
  }
}

const paypalProcessor = new PayPalPaymentProcessor();
const stripeProcessor = new StripePaymentProcessor();

const order1 = new OrderService(paypalProcessor);
const order2 = new OrderService(stripeProcessor);

console.log(order1.checkout(100));
console.log(order2.checkout(200));
