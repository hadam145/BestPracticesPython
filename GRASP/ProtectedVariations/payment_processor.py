# Třída využívající strategii – není závislá na konkrétní implementaci (GRASP: Protected Variations)
from payment_strategy import PaymentStrategy

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process(self, amount: float):
        print("[Processor] Processing payment...")
        self.strategy.pay(amount)
