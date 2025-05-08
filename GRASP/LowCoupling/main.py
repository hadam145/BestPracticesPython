# Ukázka GRASP principu Low Coupling – klient používá rozhraní, ne konkrétní implementaci
from bank_payment_processor import BankPaymentProcessor
from credit_card_processor import CardPaymentProcessor

def execute_payment(processor, amount):
    processor.process_payment(amount)

if __name__ == "__main__":
    bank = BankPaymentProcessor()
    card = CardPaymentProcessor()

    execute_payment(bank, 1200.00)
    execute_payment(card, 750.50)
