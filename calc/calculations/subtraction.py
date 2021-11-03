"""Subtraction Class"""
import pprint

from calc.calculations.calculation import Calculation

class Subtraction(Calculation):

    def getResult(self):
        difference_of_values = 0.0
        for value in self.values:
            difference_of_values =   difference_of_values - value
            pprint.pprint(value)
        return difference_of_values
