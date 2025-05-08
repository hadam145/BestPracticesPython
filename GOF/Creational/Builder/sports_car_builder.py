from car import Car
from car_builder import CarBuilder

# Konkrétní builder pro sportovní auto
class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_engine(self):
        self.car.engine = "V8 Twin Turbo"

    def set_wheels(self):
        self.car.wheels = 4

    def set_color(self):
        self.car.color = "Red"

    def get_result(self):
        return self.car
