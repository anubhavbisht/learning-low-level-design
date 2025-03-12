from abc import ABC, abstractmethod


class Notifaction(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class SMSNotification(Notifaction):
    def notify(self, message):
        print(f"Sending {message} through sms")


class EmailNotification(Notifaction):
    def notify(self, message):
        print(f"Sending {message} through email")


class NotificationFactory:
    notificationMap = {
        "email": EmailNotification,
        "sms": SMSNotification,
    }
    
    @staticmethod
    def getNotification(notificationType):
        return NotificationFactory.notificationMap.get(notificationType)()
    
notification_type = "email"
notification = NotificationFactory.getNotification(notification_type)
notification.notify("Hello, this is a factory pattern example!")
