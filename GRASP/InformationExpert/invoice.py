# Invoice má přístup k datům items, což z ní dělá nejlepšího kandidáta na výpočet celkové ceny (GRASP: Information Expert)
from item import Item

class Invoice:
    def __init__(self):
        self._items = []

    # Přidání položky do faktury
    def add_item(self, item: Item):
        self._items.append(item)

    # Výpočet celkové ceny
    def calculate_total(self) -> float:
        return sum(item.price * item.quantity for item in self._items)
