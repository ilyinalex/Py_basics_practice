from mexican_bake import MexicanBake


class PizzaSystem(object):
    __instance = None

    @staticmethod
    def get_instance():
        if PizzaSystem.__instance is None:
            PizzaSystem()
        return PizzaSystem.__instance

    def __init__(self, pizzerias):
        if PizzaSystem.__instance is None:
            PizzaSystem.__instance = self
            self.__pizzerias = pizzerias
            # self.__bakes = {"mexican": MexicanBake()}

    def get_pizzas_list(self, city):
        res = []
        for pizz in self.__pizzerias:
            if pizz.city == city:
                res.append(pizz.get_pizza_of_the_day())
        return res

    def get_pizza(self, name):
        for pizz in self.__pizzerias:
            if pizz.get_pizza_of_the_day().name == name:
                return pizz.get_pizza_of_the_day.ingredieants

    def add_pizzeria(self, pizzeria):
        self.__pizzerias.append(pizzeria)

    def rm_pizzeria(self, pizzeria):
        self.__pizzerias.remove(pizzeria)
