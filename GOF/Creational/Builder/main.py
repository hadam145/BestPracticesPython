from suv_builder import SUVBuilder
from sports_car_builder import SportsCarBuilder
from car_director import CarDirector

# Ukázka použití návrhového vzoru Builder
if __name__ == "__main__":
    print("Building SUV:")
    suv_builder = SUVBuilder()
    director = CarDirector(suv_builder)
    suv = director.construct()
    print(suv)

    print("\nBuilding Sports Car:")
    sports_builder = SportsCarBuilder()
    director = CarDirector(sports_builder)
    sports_car = director.construct()
    print(sports_car)
