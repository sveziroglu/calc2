"""Subtraction Class"""
import pprint

from calc.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        return self.value_a - self.value_b

