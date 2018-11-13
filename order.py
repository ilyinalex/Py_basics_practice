class Order(object):
    def __init__(self, client):
        self.__ord_pizzas = {}
        self.__client = client

    @property
    def pizzas(self):
        return self.__ord_pizzas

    @property
    def client(self):
        return self.__client

    def add(self, name, ingredients):
        self.__ord_pizzas[name] = ingredients
