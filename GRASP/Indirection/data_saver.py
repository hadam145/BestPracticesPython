from data_acces import DataAccess

# Třída, která neukládá data sama, ale používá zprostředkovatele (DataAccess)
class DataSaver:
    def __init__(self, data_access: DataAccess):
        self.data_access = data_access

    def save(self, data: str):
        print("[DataSaver] Delegating save operation...")
        self.data_access.save_data(data)
