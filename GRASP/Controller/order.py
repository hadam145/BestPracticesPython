# Modelová třída reprezentující objednávku
class Order:
    def __init__(self, order_id: int, customer_name: str, total_amount: float):
        self.order_id = order_id
        self.customer_name = customer_name
        self.total_amount = total_amount

    def __str__(self):
        return f"Order #{self.order_id} by {self.customer_name} for {self.total_amount:.2f} Kč"
