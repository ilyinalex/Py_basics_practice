import pizza


class MexicanPizza(pizza.Pizza):
    def __init__(self, size, default_price, default_ingredients):
        super().__init__(size, default_price, default_ingredients)
