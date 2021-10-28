"""Testing the Calculator"""
import pprint

from calc.calculator import Calculator

def test_calculator_add_static():
    """testing that our calculator has a static method for addition"""
    assert Calculator.add_numbers(1,2) == 3

def test_calculator_subtract():
    """Testing the subtract method of the calc"""
    assert Calculator.subtract_numbers(1,2) == -1

def test_calculator_multiply():
    """Testing the subtract method of the calc"""
    assert Calculator.multiply_numbers(1,2) == 2

def test_calculator_calculations_static_property():
    """Testing the subtract method of the calc"""
    pprint.pprint(Calculator.history)

    assert Calculator.add_numbers(1,2) == 3
