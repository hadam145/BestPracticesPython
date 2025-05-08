from order import Order
# Třída Customer používá a má vztah k Order – je zodpovědná za její vytvoření (GRASP: Creator)
class Customer:
    def __init__(self, name: str):
        self.name = name

    def create_order(self) -> Order:
        print(f"[Customer] {self.name} is creating a new order...")
        return Order()
