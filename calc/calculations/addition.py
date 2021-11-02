"""Addition Class"""
import pprint

from calc.calculations.calculation import Calculation

class Addition(Calculation):

    def getResult(self):
        sum_of_values = 0.0
        pprint.pprint(self.values)
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values
