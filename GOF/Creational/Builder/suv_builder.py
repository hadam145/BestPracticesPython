from car import Car
from car_builder import CarBuilder

# Konkrétní builder pro SUV - implementuje kroky stavby
class SUVBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_engine(self):
        self.car.engine = "V6"

    def set_wheels(self):
        self.car.wheels = 4

    def set_color(self):
        self.car.color = "Black"

    def get_result(self):
        return self.car
