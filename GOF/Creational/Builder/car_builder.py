from abc import ABC, abstractmethod

# Rozhraní pro builder - definuje kroky pro sestavení objektu
class CarBuilder(ABC):
    @abstractmethod
    def set_engine(self): pass

    @abstractmethod
    def set_wheels(self): pass

    @abstractmethod
    def set_color(self): pass

    @abstractmethod
    def get_result(self): pass
