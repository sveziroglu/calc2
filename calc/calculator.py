""" This is the increment function"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication

class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def add_numbers(value_a, value_b):
        """ adds two numbers"""
        addition = Addition(value_a, value_b)
        Calculator.history.append(addition)
        return addition.getResult()

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ subtract number from result"""
        return Subtraction.subtract(value_a,value_b)
    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ subtract number from result"""
        return Multiplication.multiply(value_a,value_b)
