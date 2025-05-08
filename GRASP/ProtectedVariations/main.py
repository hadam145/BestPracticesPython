# Ukázka GRASP principu Protected Variations – klient není závislý na konkrétní třídě
from paypal_payment import PaypalPayment
from payment_processor import PaymentProcessor

if __name__ == "__main__":
    strategy = PaypalPayment()
    processor = PaymentProcessor(strategy)
    processor.process(299.99)
