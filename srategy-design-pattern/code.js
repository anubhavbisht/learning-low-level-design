class PaymentStrategy {
  pay(amount) {
    throw new Error("Method 'pay()' must be implemented.");
  }
}

class PayPalPayment extends PaymentStrategy {
  pay(amount) {
    console.log(`Paid ${amount} via PayPal`);
  }
}

class StripePayment extends PaymentStrategy {
  pay(amount) {
    console.log(`Paid ${amount} via Stripe`);
  }
}

class BitcoinPayment extends PaymentStrategy {
  pay(amount) {
    console.log(`Paid ${amount} via Bitcoin`);
  }
}

class PaymentProcessor {
  constructor(strategy) {
    this.strategy = strategy;
  }

  processPayment(amount) {
    this.strategy.pay(amount);
  }
}

const paypalProcessor = new PaymentProcessor(new PayPalPayment());
const stripeProcessor = new PaymentProcessor(new StripePayment());
const bitcoinProcessor = new PaymentProcessor(new BitcoinPayment());

paypalProcessor.processPayment(100);
stripeProcessor.processPayment(200);
bitcoinProcessor.processPayment(300);
