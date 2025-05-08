from order_controller import OrderController
# Ukázka GRASP principu Controller - řízení logiky objednávek přes prostředníka
if __name__ == "__main__":
    controller = OrderController()
    controller.create_order(1, "Alice", 1500.00)
    controller.create_order(2, "Bob", 2300.00)

    print("\nAll orders:")
    for o in controller.get_all_orders():
        print(o)

    print("\nFinding order #1:")
    found = controller.find_order_by_id(1)
    print(found)
