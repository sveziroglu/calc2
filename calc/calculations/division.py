"""This is the division class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """This is division"""

    def get_result(self):
        """This gives the quotient"""
        quotient = self.values[0]
        divisor = self.values[1]
        final = quotient/divisor
        return final
