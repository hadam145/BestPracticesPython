# Rozhraní pro přístup k datům – není svázáno s konkrétní doménou (GRASP: Pure Fabrication)
from abc import ABC, abstractmethod

class DataService(ABC):
    @abstractmethod
    def fetch_data(self):
        pass
