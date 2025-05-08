from abc import ABC, abstractmethod

# Rozhraní pro přístup k datům
class DataAccess(ABC):
    @abstractmethod
    def save_data(self, data: str):
        pass
