# Fish je podtřída, ale chování předefinuje tak, že může způsobit poruchu v nadtřídě
from animal import Animal

class Fish(Animal):
    def move(self):
        raise NotImplementedError("Fish cannot move this way")
