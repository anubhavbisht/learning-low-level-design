from ObserverInterface import NotificationAlertObserver
from ObservableInterface import StockObservable

class EmailAlertObserver(NotificationAlertObserver):
    def __init__(self, emailId: str, observable: StockObservable):
        self.emailId = emailId
        self.observable = observable

    def update(self):
        stockCount = self.observable.getStock()
        print(
            f"Sending mail to {self.emailId}.Stock is now available stock count::{stockCount}"
        )
