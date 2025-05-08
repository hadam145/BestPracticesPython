# Ukázka DIP – můžeme snadno změnit implementaci notifieru bez zásahu do služby
from notification_service import NotificationService
from email_notifier import EmailNotifier

if __name__ == "__main__":
    service = NotificationService(EmailNotifier())
    service.notify("Hello from DIP world!")
