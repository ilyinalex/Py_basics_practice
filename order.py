class Order(object):
    def __init__(self, pizzas):
        self.__pizzas = pizzas

    @property
    def pizzas(self):
        return self.__pizzas
