# Konkrétní implementace – platba přes kreditní kartu
from payment_processor import PaymentProcessor

class CardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"[Card] Processing credit card payment for {amount:.2f} Kč")
