"""Testing the Calculator"""
import pprint

from calc.calculator import Calculator

def test_calculator_add_static():
    """testing that our calculator has a static method for addition"""
    assert Calculator.add_numbers(1.0,2.0) == 3.0

def test_calculator_subtract():
    """Testing the subtract method of the calc"""
    assert Calculator.subtract_numbers(1.0,2.0) == -3.0

def test_calculator_multiply():
    """Testing the subtract method of the calc"""
    assert Calculator.multiply_numbers(1.0,2.0) == 2.0

def test_calculator_history_static_property():
    """Testing the subtract method of the calc"""
    Calculator.add_numbers(1.0,2.0)
    assert len(Calculator.history) == 3

def test_calculator_history_getAddtionCalculation():
    calculation = Calculator.history[0]
    assert calculation.getResult()  == 3.0
