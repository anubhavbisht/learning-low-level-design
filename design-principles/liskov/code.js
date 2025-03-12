class Bird {
  fly() {
    return "I can fly!";
  }
}

class Penguin extends Bird {
  fly() {
    throw new Error("Penguins can't fly!");
  }
}

function makeBirdFly(bird) {
  console.log(bird.fly());
}

const sparrow = new Bird();
const penguin = new Penguin();

console.log(makeBirdFly(sparrow));
console.log(makeBirdFly(penguin));

class Bird {
  fly() {
    return "I can fly!";
  }
}

class Penguin extends Bird {
  // ❌ Violates LSP
  fly() {
    throw new Error("Penguins can't fly!");
  }
}

// Usage
function makeBirdFly(bird) {
  console.log(bird.fly());
}

const sparrow = new Bird();
const penguin = new Penguin();

console.log(makeBirdFly(sparrow)); // ✅ "I can fly!"
console.log(makeBirdFly(penguin)); // ❌ Error: Penguins can't fly!

class NewBird {
  makeSound() {
    return "Some generic bird sound";
  }
}

class FlyingBird extends NewBird {
  fly() {
    return "I can fly!";
  }
}

class NonFlyingBird extends NewBird {
  fly() {
    return "I can't fly!";
  }
}

class Sparrow extends FlyingBird {
  makeSound() {
    return "Chirp!";
  }
}

class Penguin extends NonFlyingBird {
  makeSound() {
    return "Honk!";
  }
}

function makeBirdFly(bird) {
  console.log(bird.fly());
}

const sparrow1 = new Sparrow();
const penguin1= new Penguin();

console.log(makeBirdFly(sparrow1)); 
console.log(makeBirdFly(penguin1)); 
