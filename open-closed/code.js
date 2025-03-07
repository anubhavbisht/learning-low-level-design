class Discount {
  getDiscount(customerType, price) {
    if (customerType === "regular") {
      return price * 0.9;
    } else if (customerType === "vip") {
      return price * 0.8;
    } else {
      return price;
    }
  }
}

const discount = new Discount();
console.log(discount.getDiscount("regular", 100)); // 90
console.log(discount.getDiscount("vip", 100)); // 80

class NewDiscount {
  applyDiscount(price) {
    return price;
  }
}

class RegularDiscount extends Discount {
  applyDiscount(price) {
    return price * 0.9;
  }
}

class VIPDiscount extends Discount {
  applyDiscount(price) {
    return price * 0.8;
  }
}

class SuperVIPDiscount extends Discount {
  applyDiscount(price) {
    return price * 0.7;
  }
}

function calculateDiscount(price, discountStrategy) {
  return discountStrategy.applyDiscount(price);
}

console.log(calculateDiscount(100, new RegularDiscount()));
console.log(calculateDiscount(100, new VIPDiscount()));
console.log(calculateDiscount(100, new SuperVIPDiscount()));
