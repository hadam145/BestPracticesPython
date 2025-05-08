# Porušení OCP – musíme upravovat metodu při přidání nové varianty
class PaymentService:
    def pay(self, method: str, amount: float):
        if method == "card":
            print(f"[Card] Paid {amount:.2f} Kč with card")
        elif method == "paypal":
            print(f"[PayPal] Paid {amount:.2f} Kč with PayPal")
        else:
            print("[Error] Unknown payment method")
