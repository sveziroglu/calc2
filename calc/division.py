"""This is the division class"""
from calc.calculation import Calculation

class Division(Calculation):
    """This is division"""
    def get_result(self):
        """This gives the quotient"""
        return self.value_a / self.value_b
