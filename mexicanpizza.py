import pizza


class MexicanPizza(pizza.Pizza):
    def __init__(self, default_size, default_price, default_ingredients, name):
        super().__init__(default_size, default_price, default_ingredients, name)

