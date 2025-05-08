# Správně implementovaná podtřída – dodržuje smluvené chování
from animal import Animal

class Dog(Animal):
    def make_sound(self):
        print("Woof")
