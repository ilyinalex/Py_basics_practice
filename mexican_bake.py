from bake import Bake
from mexicanpizza import MexicanPizza


class MexicanBake(Bake):
    def __init__(self, default_size, default_price, default_ingredients):
        self.__default_price = default_price
        self.__default_size = default_size
        self.__default_ingredients = default_ingredients

    def cook(self):
        return MexicanPizza(self.__default_size, self.__default_price, self.__default_ingredients)