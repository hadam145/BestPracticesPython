# Rozhraní pro různé způsoby platby (strategie) – GRASP: Protected Variations
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass
