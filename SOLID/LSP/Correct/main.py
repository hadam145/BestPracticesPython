# Ukázka LSP – obě podtřídy se dají zaměnit bez rozbití kódu
from dog import Dog
from cat import Cat

def animal_sound(animal):
    animal.make_sound()

if __name__ == "__main__":
    animal_sound(Dog())
    animal_sound(Cat())
