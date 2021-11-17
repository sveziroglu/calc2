"""Testing the Calculator"""
import pprint
import pytest
from calculator.calculator import Calculator

@pytest.fixture
def clear_history():
    """clears history"""
    Calculator.clear_history()

def test_get_history(clear_history):
    """testing pulling up history"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    assert Calculator.add_number(2,2) == 4
    assert Calculator.divide_numbers(25,5) == 5
    assert Calculator.multiply_numbers(7,7) == 49
    assert Calculator.get_history() == Calculator.history

def test_get_last_calculation_result(clear_history):
    """testing calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_last_calculation_added_to_history() == 5

def test_get_first_calculation_result(clear_history):
    """testing calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    assert Calculator.add_number(6, 2) == 8
    assert Calculator.add_number(5, 2) == 7
    assert Calculator.get_result_of_first_calculation_added_to_history() == 8

def test_clear_history(clear_history):
    """testing calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    assert Calculator.add_number(7,3) == 10
    assert Calculator.add_number(6, 6) == 12
    assert Calculator.add_number(7, 7) == 14
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.clear_history() is True
    assert Calculator.history_count() == 0

def test_count_history(clear_history):
    """testing calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    assert Calculator.history_count() == 0
    assert Calculator.add_number(8, 8) == 16
    assert Calculator.add_number(9, 9) == 18
    assert Calculator.history_count() == 2

def test_calculator_add(clear_history):
    """testing addition on calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    assert Calculator.add_number(7,3) == 10
    assert Calculator.add_number(6, 6) == 12
    assert Calculator.add_number(7, 7) == 14
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)

def test_calculator_subtract(clear_history):
    """testing calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    assert Calculator.subtract_number(1, 2) == -1

def test_calculator_multiply(clear_history):
    """testing calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    assert Calculator.multiply_numbers(1,2) == 2

def test_calculator_division(clear_history):
    """testing calculator"""
    # pylint: disable=redefined-outer-name
    # pylint: disable=unused-argument
    assert Calculator.divide_numbers(6,3) == 2
