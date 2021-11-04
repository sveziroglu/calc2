"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculator.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(1.0) == 1.0

def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_numbers(1.0,2.0) == -3.0

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(1.0,2.0) == 2.0

