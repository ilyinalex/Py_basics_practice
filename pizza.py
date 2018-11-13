class Pizza:
    def __init__(self, size, default_price, default_ingredients):
        self._size = size
        self._price = default_price
        self._ingredients = default_ingredients
        self.calculate_price()

    def add_ingredient(self, ingredient):
        self._ingredients.append(ingredient)

    def calculate_price(self):
        for ingr in self._ingredients:
            self._price += ingr.price
