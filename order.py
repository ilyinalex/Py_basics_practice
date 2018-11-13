class Order(object):
    def __init__(self, client, pizza, ingredients):
        self.__client = client
        self.__pizza = pizza
        self.__ingredients = ingredients

    @property
    def client(self):
        return self.__client

    @property
    def pizza(self):
        return self.__pizza

    @property
    def ingredients(self):
        return self.__ingredients
