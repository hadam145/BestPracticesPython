# Rozšíření bez úpravy původní logiky
from payment_processor import PaymentProcessor

class CreditCardPayment(PaymentProcessor):
    def pay(self, amount: float):
        print(f"[CreditCard] Paid {amount:.2f} Kč using credit card")
