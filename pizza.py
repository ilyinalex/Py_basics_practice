class Pizza:
    def __init__(self, size, default_price, default_ingredients, name):
        self._size = size
        self._price = default_price
        self._ingredients = default_ingredients
        self.calculate_price()
        self._name = name

    def add_ingredient(self, ingredient):
        self._ingredients.append(ingredient)

    def calculate_price(self):
        for ingr in self._ingredients:
            self._price += ingr.price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        _size = size

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        self._ingredients = ingredients

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self.name = name
