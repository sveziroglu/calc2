from calc.calculation import Calculation

class Division(Calculation):
    def __init__(self, div_1, div_2):
        super().__init__(div_1, div_2)
        self.div_2 = any()
        self.div_1 = any()

    def getResult(self):
        return self.div_1/self.div_2