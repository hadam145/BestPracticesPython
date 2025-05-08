# Porušení DIP – závislost na konkrétní třídě
class NotificationService:
    def notify(self, message: str):
        email = EmailNotifier()
        email.send_email(message)

class EmailNotifier:
    def send_email(self, message: str):
        print(f"[Email] Sending: {message}")
