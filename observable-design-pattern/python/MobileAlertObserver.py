from ObserverInterface import NotificationAlertObserver
from ObservableInterface import StockObservable

class MobileAlertObserver(NotificationAlertObserver):
    def __init__(self, phone: str, observable: StockObservable):
        self.phone = phone
        self.observable = observable

    def update(self):
        stockCount = self.observable.getStock()
        print(
            f"Sending sms to {self.phone}.Stock is now available stock count::{stockCount}"
        )