from customer import Customer
# Ukázka GRASP principu Creator – objekt, který používá jiný objekt, je zodpovědný za jeho vytvoření
if __name__ == "__main__":
    customer = Customer("Eva Nováková")
    order = customer.create_order()
    print(order)
