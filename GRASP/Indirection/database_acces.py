from data_acces import DataAccess

# Implementace rozhraní DataAccess - přímo ukládá data
class DatabaseAccess(DataAccess):
    def save_data(self, data: str):
        print(f"[Database] Saving data: {data}")
