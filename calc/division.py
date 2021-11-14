"""This is the division"""
from calc.calculation import Calculation
#This class is for dividing value_a and value_b
class Division(Calculation):
    """this will get the quotient"""
    def get_result(self):
        """this will get the quotient"""
        return self.value_a / self.value_b
