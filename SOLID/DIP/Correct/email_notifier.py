# Konkrétní implementace notifieru – e-mail
from notifier import Notifier

class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"[Email] Sending: {message}")
