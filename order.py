class Order(object):
    def __init__(self, client):
        self.__ord_pizzas = {}
        self.__client = client

    @property
    def ord_pizzas(self):
        return self.__ord_pizzas

    @ord_pizzas.setter
    def ord_pizzas(self, ord_pizzas_and_ingredients):
        self.__ord_pizzas = ord_pizzas_and_ingredients

    def add(self, name, ingredients):
        self.__ord_pizzas[name] = ingredients
