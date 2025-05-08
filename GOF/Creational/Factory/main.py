from factory import Factory

# Ukázka použití návrhového vzoru Factory
if __name__ == "__main__":
    for type_ in ["A", "B"]:
        product = Factory.create_product(type_)
        print(f"Created {type_}: {product.operation()}")
