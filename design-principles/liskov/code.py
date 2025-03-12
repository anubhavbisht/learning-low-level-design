class Bird:
    def fly(self):
        return "I can fly!"

class Penguin(Bird):  
    def fly(self):
        raise NotImplementedError("Penguins can't fly!")


def make_bird_fly(bird: Bird):
    print(bird.fly())


sparrow = Bird()
penguin = Penguin()

print(make_bird_fly(sparrow))   
print(make_bird_fly(penguin))  

from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        return "I can fly!"

class NonFlyingBird(Bird):
    def fly(self):
        return "I can't fly!"

class Sparrow(FlyingBird):
    def make_sound(self):
        return "Chirp!"

class Penguin(NonFlyingBird):
    def make_sound(self):
        return "Honk!"

def make_bird_fly(bird: FlyingBird):
    print(bird.fly())

sparrow = Sparrow()
penguin = Penguin()

print(make_bird_fly(sparrow))
