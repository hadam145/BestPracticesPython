# Další podtřída – rovněž se chová korektně podle nadtřídy
from animal import Animal

class Cat(Animal):
    def make_sound(self):
        print("Meow")
