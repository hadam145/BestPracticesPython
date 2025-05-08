from concrete_product_a import ConcreteProductA
from concrete_product_b import ConcreteProductB

# Továrna, která vytváří produkty na základě vstupu
class Factory:
    @staticmethod
    def create_product(product_type: str):
        if product_type == "A":
            return ConcreteProductA()
        elif product_type == "B":
            return ConcreteProductB()
        else:
            raise ValueError(f"Unknown product type: {product_type}")
