# Ukázka GRASP principu Polymorphism – různé třídy reagují různě na stejnou zprávu
from cat import Cat
from dog import Dog

def make_animal_sound(animal):
    animal.make_sound()

if __name__ == "__main__":
    animals = [Cat(), Dog()]
    for a in animals:
        make_animal_sound(a)
