""" This is the increment function"""
from calc.history.calculations import Calculations

#the calculator class just contains the methods to calculate
class Calculator:
    """ This is the Calculator class"""
    #the calculator class just calls methods on Calculations class
    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        return Calculations.add_addition_calculation(args)
    #Args allows me to pass in as many parameters as a I want, it becomes a tuple of values
    @staticmethod
    def subtract_numbers(*args):
        """ subtract a list of numbers from result"""
        return Calculations.add_subtraction_calculation(args)
    @staticmethod
    def multiply_numbers(*args):
        """ multiplication number from result"""
        return Calculations.add_multiplication_calculation(args)

