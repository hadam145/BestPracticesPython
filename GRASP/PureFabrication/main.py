# Ukázka GRASP principu Pure Fabrication – třídy vytvořené pro zajištění struktury a odpovědnosti
from data_service_proxy import DataServiceProxy
from logger import Logger

if __name__ == "__main__":
    service = DataServiceProxy()
    data = service.fetch_data()
    Logger.log(f"Data received: {data}")
