# Třída reprezentující položku faktury s cenou a množstvím
class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
