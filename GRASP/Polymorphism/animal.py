# Nadřazená třída – definuje polymorfní metodu make_sound()
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
