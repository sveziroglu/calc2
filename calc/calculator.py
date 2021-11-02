""" This is the increment function"""
import pprint

from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication

class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def add_numbers(*args):
        """ adds two numbers"""
        addition = Addition(args)
        Calculator.history.append(addition)
        return addition.getResult()
    @staticmethod
    def clear_history():
        Calculator.history.clear()
    @staticmethod
    def get_calculation(num):
        return Calculator.history[num]
    @staticmethod
    def get_calculation_last():
        return Calculator.history[-1]
    @staticmethod
    def subtract_numbers(*args):
        """ subtract number from result"""
        subtraction = Subtraction(args)
        Calculator.history.append(subtraction)
        return subtraction.getResult()
    @staticmethod
    def multiply_numbers(*args):
        """ multiplication number from result"""
        multiplication = Multiplication(args)
        return multiplication.getResult()
