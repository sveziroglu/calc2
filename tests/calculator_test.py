"""Testing the Calculator"""
import pprint

import pytest

from calc.calculator import Calculator

#this is how you define a function that will run each time you pass it to a test, it is called a fixture
@pytest.fixture
def clear_history():
    Calculator.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history):
    """testing that our calculator has a static method for addition"""
    assert Calculator.add_numbers(1.0) == 1.0

def test_calculator_subtract_static(clear_history):
    """Testing the subtract method of the calc"""
    assert Calculator.subtract_numbers(1.0,2.0) == -3.0

def test_calculator_multiply_static(clear_history):
    """Testing the subtract method of the calc"""
    assert Calculator.multiply_numbers(1.0,2.0) == 2.0

def test_calculator_history_static_property(clear_history):
    """Testing the subtract method of the calc"""
    Calculator.add_numbers(1.0,2.0)
    assert len(Calculator.history) == 1

def test_clear_history():
    Calculator.add_numbers(1.0,2.0)
    assert Calculator.clear_history() == True

def test_get_calculation():
    Calculator.add_numbers(1.0,2.0)
    assert Calculator.get_calculation(0).getResult() == 3

def test_get_calculation_last():
    Calculator.add_numbers(1.0,2.0)
    assert Calculator.get_calculation_last().getResult() == 3