from abc import ABC, abstractmethod


class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Robot(Worker):
    def work(self):
        return "Robot is working"

    def eat(self):
        raise NotImplementedError("Robots don't eat!")


robot = Robot()
print(robot.work())
print(robot.eat())

from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        return "Human is working"

    def eat(self):
        return "Human is eating"

class Robot(Workable):
    def work(self):
        return "Robot is working"

human = Human()
robot = Robot()

print(human.work())  
print(human.eat())   
print(robot.work())  

