"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):

    def getResult(self):
        product_of_values = 0.0
        for value in self.values:
            product_of_values = value * product_of_values
        return product_of_values