# Proxy, který kontroluje nebo rozšiřuje přístup k reálné službě
from data_service import DataService
from real_data_service import RealDataService

class DataServiceProxy(DataService):
    def __init__(self):
        self._real_service = RealDataService()

    def fetch_data(self):
        print("[Proxy] Logging access to real data service...")
        return self._real_service.fetch_data()
