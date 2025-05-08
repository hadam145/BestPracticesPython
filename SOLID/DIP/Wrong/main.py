# Ukázka porušení DIP – není možné snadno zaměnit implementaci bez přímého zásahu do služby
from notification_service import NotificationService

if __name__ == "__main__":
    service = NotificationService()
    service.notify("This is tightly coupled!")
