# Abstraktní třída pro zpracování plateb (rozhraní podle GRASP: Low Coupling)
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass
