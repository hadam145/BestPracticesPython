# Jednoduchá třída reprezentující objednávku
class Order:
    def __init__(self):
        self.status = "Created"

    def __str__(self):
        return f"Order status: {self.status}"
