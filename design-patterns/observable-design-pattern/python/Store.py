from ApplePhoneObservable import ApplePhoneObservable
from ObservableInterface import StockObservable
from ObserverInterface import NotificationAlertObserver
from MobileAlertObserver import MobileAlertObserver
from EmailAlertObserver import EmailAlertObserver

applePhoneObservable: StockObservable = ApplePhoneObservable()

observer1: NotificationAlertObserver = MobileAlertObserver(
    "99911", applePhoneObservable
)

observer2: NotificationAlertObserver = MobileAlertObserver(
    "99911", applePhoneObservable
)

observer3: NotificationAlertObserver = EmailAlertObserver(
    "xyz@gmail.com", applePhoneObservable
)

applePhoneObservable.addObserver(observer1)
applePhoneObservable.addObserver(observer2)
applePhoneObservable.addObserver(observer3)

applePhoneObservable.setStock(10)