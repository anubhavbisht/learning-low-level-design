class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  validate() {
    return this.email.includes("@");
  }

  save() {
    console.log(`Saving ${this.name} to the database`);
  }
}

const user = new User("Alice", "alice@example.com");
if (user.validate()) {
  user.save();
}

class NewUser {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }
}

class UserValidator {
  static isValid(user) {
    return user.email.includes("@");
  }
}

class UserRepository {
  static save(user) {
    console.log(`Saving ${user.name} to the database`);
  }
}

const newuser = new NewUser("Alice", "alice@example.com");

if (UserValidator.isValid(newuser)) {
  UserRepository.save(newuser);
}
