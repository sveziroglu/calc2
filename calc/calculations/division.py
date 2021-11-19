"""This is division"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """Division calculation"""

    def get_result(self, value=1):
        """This gets the quotient"""
        quotient = self.values[1]
        quotient = quotient / value
        return quotient
