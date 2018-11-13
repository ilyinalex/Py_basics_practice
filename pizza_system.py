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
            self.__bakes = {"mexican": MexicanBake()}

    def add_pizzeria(self, pizzeria):
        self.__pizzerias.append(pizzeria)

    def rm_pizzeria(self, pizzeria):
        self.__pizzerias.remove(pizzeria)
