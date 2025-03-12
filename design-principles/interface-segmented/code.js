class CreditCardProcessor {
  processCreditCard() {
    throw new Error("Method must be implemented");
  }
}

class PayPalProcessor {
  processPayPal() {
    throw new Error("Method must be implemented");
  }
}

class CryptoProcessor {
  processCrypto() {
    throw new Error("Method must be implemented");
  }
}

class CreditCardPayment extends CreditCardProcessor {
  processCreditCard() {
    return "Processing credit card payment";
  }
}

class PayPalPayment extends PayPalProcessor {
  processPayPal() {
    return "Processing PayPal payment";
  }
}

class CryptoPayment extends CryptoProcessor {
  processCrypto() {
    return "Processing Crypto payment";
  }
}
