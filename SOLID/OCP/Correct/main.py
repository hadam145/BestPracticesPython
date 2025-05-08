# OCP správně – rozšiřujeme pomocí nových tříd, nepřepisujeme staré
from credit_card_payment import CreditCardPayment
from paypal_payment import PaypalPayment

def process_payment(payment_processor, amount):
    payment_processor.pay(amount)

if __name__ == "__main__":
    process_payment(CreditCardPayment(), 300)
    process_payment(PaypalPayment(), 150)
