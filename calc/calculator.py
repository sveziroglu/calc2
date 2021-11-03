""" This is the increment function"""
import pprint

from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication

class Calculator:
    """ This is the Calculator class"""
    history = []
    @staticmethod
    def convert_args_to_list_float(values):
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float
    @staticmethod
    def add_numbers(*args):
        """ adds two numbers"""
        addition = Addition(Calculator.convert_args_to_list_float(args))
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
        subtraction = Subtraction(Calculator.convert_args_to_list_float(args))
        Calculator.history.append(subtraction)
        return subtraction.getResult()
    @staticmethod
    def multiply_numbers(*args):
        """ multiplication number from result"""
        multiplication = Multiplication(Calculator.convert_args_to_list_float(args))
        return multiplication.getResult()
