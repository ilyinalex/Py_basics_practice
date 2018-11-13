class Bake:
    __instance = None

    @staticmethod
    def get_instance():
        if Bake.__instance is None:
            Bake()
        return Bake.__instance

    def cook(self):
        pass

    def __init__(self):
        if Bake.__instance is None:
            Bake.__instance = self
