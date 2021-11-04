"""Calculation history Class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
class Calculations:
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        return Calculations.history[-1]
    @staticmethod
    def get_first_calculation():
        return Calculations.history[-1]
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation(values):
        Calculations.add_calculation(Addition(values))
        return Calculations.get_last_calculation().get_result()
    @staticmethod
    def add_subtraction_calculation(values):
        Calculations.add_calculation(Subtraction(values))
        return Calculations.get_last_calculation().get_result()
    @staticmethod
    def add_multiplication_calculation(values):
        Calculations.add_calculation(Multiplication(values))
        return Calculations.get_last_calculation().get_result()