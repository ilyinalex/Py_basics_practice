class Client(object):
    def __init__(self, f_name, s_name, city):
        self.__first_name = f_name
        self.__second_name = s_name
        self.__city = city

    @property
    def first_name(self):
        return self.__firstName

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

    def create_order(self):
        pass
