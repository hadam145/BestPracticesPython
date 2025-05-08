from database_acces import DatabaseAccess
from data_saver import DataSaver

# Ukázka principu GRASP - Indirection
if __name__ == "__main__":
    db = DatabaseAccess()
    saver = DataSaver(db)
    saver.save("Test GRASP – Indirection")
