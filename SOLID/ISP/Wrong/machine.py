# Velké rozhraní – klient musí implementovat vše, i když to nepotřebuje
from abc import ABC, abstractmethod

class Machine(ABC):
    @abstractmethod
    def print_document(self, document: str):
        pass

    @abstractmethod
    def scan_document(self, document: str):
        pass
