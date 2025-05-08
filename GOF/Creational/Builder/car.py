# Reprezentuje výsledný objekt, který sestavujeme
class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return f"Car with {self.engine} engine, {self.wheels} wheels, color {self.color}"
