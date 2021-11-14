"""This subtracts from value a and value b"""

from calc.calculation import Calculation

#This uses calculation from parent folder
class Subtraction(Calculation):
    """This will result in the difference"""
    def get_result(self):
        """This will result in the difference"""
        return self.value_a - self.value_b
