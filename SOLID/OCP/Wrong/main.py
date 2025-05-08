# Ukázka porušení OCP – logika je centralizovaná a musí se měnit při každém rozšíření
from payment_service import PaymentService

if __name__ == "__main__":
    service = PaymentService()
    service.pay("card", 300)
    service.pay("paypal", 150)
