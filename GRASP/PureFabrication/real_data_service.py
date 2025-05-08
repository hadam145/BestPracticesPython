# Reálná implementace služby – získává data z úložiště
from data_service import DataService

class RealDataService(DataService):
    def fetch_data(self):
        print("[RealDataService] Fetching data from the database...")
        return {"data": "Real data from DB"}
