# Konkrétní implementace strategie – platba přes PayPal
from payment_strategy import PaymentStrategy

class PaypalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"[PayPal] Paying {amount:.2f} Kč via PayPal")
