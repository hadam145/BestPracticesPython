# Další malé rozhraní – nezatěžuje třídu, která nechce skenovat
from abc import ABC, abstractmethod

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document: str):
        pass
