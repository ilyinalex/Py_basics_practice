import order


class Client(object):
    def __init__(self, f_name, s_name, city, system):
        self.__first_name = f_name
        self.__second_name = s_name
        self.__city = city
        self.__system = system

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, f_name):
        self.__first_name = f_name

    @property
    def second_name(self):
        return self.__second_name

    @second_name.setter
    def second_name(self, s_name):
        self.__second_name = s_name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    def create_order(self, pizzas_and_ingredients):
        new_order = order.Order(self, pizzas_and_ingredients)
        self.__system.process(new_order)

    def __str__(self):
        return "Client: " + self.__first_name + " " + self.__second_name + "\nCity: " + self.__city
