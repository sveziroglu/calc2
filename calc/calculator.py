""" This is the increment function"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication

class Calculator:
    """ This is the Calculator class"""
    history = []
    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        addition = Addition(args)
        Calculator.history.append(addition)
        return addition.get_result()

    @staticmethod
    def subtract_numbers(*args):
        """ subtract a list of numbers from result"""
        subtraction = Subtraction(args)
        Calculator.history.append(subtraction)
        return subtraction.get_result()
    @staticmethod
    def multiply_numbers(*args):
        """ multiplication number from result"""
        multiplication = Multiplication(args)
        return multiplication.get_result()
