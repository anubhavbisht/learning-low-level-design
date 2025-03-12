from abc import ABC, abstractmethod
from ObserverInterface import NotificationAlertObserver

class StockObservable(ABC):
    @abstractmethod
    def addObserver(self, observer: NotificationAlertObserver):
        pass

    @abstractmethod
    def removeObserver(self, observer: NotificationAlertObserver):
        pass

    @abstractmethod
    def notifyObserver(self):
        pass

    @abstractmethod
    def setStock(self):
        pass

    @abstractmethod
    def getStock(self):
        pass
