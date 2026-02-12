class Fieza:
    @staticmethod
    def destruirPlaneta():
        ...

class Sayian:
    poblacio = 0

    def __init__(self):
        Sayian.poblacio += 1
        if Sayian.poblacio == 10:
            Sayian.destruirPlaneta()

    @staticmethod
    def destruirPlaneta():
        Frieza.destruirPlaneta()

