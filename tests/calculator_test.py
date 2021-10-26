"""Testing the Calculator"""
from calc.calculator import Calculator

def test_calculator_add_static():
    """testing that our calcultor has a static method for addition"""
    assert Calculator.add_numbers(1,2) == 3

def test_calculator_subtract():
    """Testing the subtract method of the calc"""

    assert Calculator.subtract_numbers(1,2) == -1
