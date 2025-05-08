from abc import ABC, abstractmethod

# Abstraktní produkt - definuje společné rozhraní pro všechny produkty
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass
