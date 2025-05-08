# Porušení LSP – Fish sice dědí, ale nelze ji použít jako běžné Animal
from fish import Fish

if __name__ == "__main__":
    animal = Fish()
    animal.move()  # výjimka – porušení substituce
