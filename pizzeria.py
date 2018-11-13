import datetime


class Pizzeria(object):
    def __init__(self, title, city, default_pizzas):
        self.__title = title
        self.__city = city
        self.__current_day = datetime.datetime.now().weekday()
        self.__default_pizzas = default_pizzas
        self.__bakes = {}

    def add_bake(self, pizzas_name, bake):
        self.__bakes[pizzas_name] = bake

    @property
    def title(self):
        return self.__title

    @title.setter
    def city(self, title):
        self.__title = title

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def current_day(self):
        return self.__current_day

    def get_pizza_of_the_day(self):
        return self.__default_pizzas[self.__current_day]
