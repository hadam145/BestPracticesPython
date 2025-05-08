# Konkrétní implementace – platba přes bankovní převod
from payment_processor import PaymentProcessor

class BankPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"[Bank] Processing bank transfer of {amount:.2f} Kč")
