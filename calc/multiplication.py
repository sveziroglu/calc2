"""This is multiplication"""
from calc.calculation import Calculation
#This will multiply value_a and value_b
class Multiplication(Calculation):
    """This will be the product"""
    def get_result(self):
        """this will get the product"""
        return self.value_a * self.value_b
