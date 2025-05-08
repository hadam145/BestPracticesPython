# Další rozšíření, které nijak nemění ostatní části systému
from payment_processor import PaymentProcessor

class PaypalPayment(PaymentProcessor):
    def pay(self, amount: float):
        print(f"[PayPal] Paid {amount:.2f} Kč via PayPal")
