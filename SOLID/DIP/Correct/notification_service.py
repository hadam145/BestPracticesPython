# Vyšší vrstva závisí na abstrakci, ne na konkrétní třídě
from notifier import Notifier

class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send(message)
