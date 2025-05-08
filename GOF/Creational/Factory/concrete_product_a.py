from product import Product

# Konkrétní produkt A - implementace metody operation
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductA"
