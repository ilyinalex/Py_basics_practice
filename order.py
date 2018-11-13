class Order(object):
    def __init__(self):
        self.__ord_pizzas = {}

    @property
    def pizzas(self):
        return self.__ord_pizzas

    def add(self, name, ingredients):
        self.__ord_pizzas[name] = ingredients;