from product import Product

# Konkrétní produkt B - implementace metody operation
class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductB"
