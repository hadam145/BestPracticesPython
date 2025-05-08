from order import Order
# Třída Controller podle GRASP - zprostředkovává komunikaci a obsahuje aplikační logiku
class OrderController:
    def __init__(self):
        self.orders = []

    def create_order(self, order_id: int, customer_name: str, total_amount: float):
        order = Order(order_id, customer_name, total_amount)
        self.orders.append(order)
        print(f"[Controller] Order created: {order}")
        return order

    def get_all_orders(self):
        return self.orders

    def find_order_by_id(self, order_id: int):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        print(f"[Controller] Order with ID {order_id} not found.")
        return None
