# Malé a specifické rozhraní – oddělené podle odpovědností
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document: str):
        pass
