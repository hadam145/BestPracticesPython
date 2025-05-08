# Řídící třída, která sestavuje auto pomocí builderu
class CarDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.set_engine()
        self._builder.set_wheels()
        self._builder.set_color()
        return self._builder.get_result()
