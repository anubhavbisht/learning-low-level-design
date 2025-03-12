from typing import List
from ObservableInterface import StockObservable
from ObserverInterface import NotificationAlertObserver

class ApplePhoneObservable(StockObservable):
    def __init__(self):
        self.stockCount = 0
        self.observers: List[NotificationAlertObserver] = []

    def addObserver(self, observer: NotificationAlertObserver):
        self.observers.append(observer)

    def removeObserver(self, observer: NotificationAlertObserver):
        self.observers.remove(observer)

    def notifyObserver(self):
        for observer in self.observers:
            observer.update()

    def setStock(self, amount):
        prev=self.stockCount
        self.stockCount = amount
        if prev == 0:
            self.notifyObserver()
        
    def getStock(self):
        return self.stockCount