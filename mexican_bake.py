from bake import Bake
from mexicanpizza import MexicanPizza


class MexicanBake(Bake):
    def __init__(self, default_size, default_price, default_ingredients):
        self.default_price = default_price
        self.default_size = default_size
        self.default_ingredients = default_ingredients

    def cook(self):
        return MexicanPizza(self.default_size, self.default_price, self.default_ingredients)
