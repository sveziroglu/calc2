"""Testing the Calculator"""
import pprint

import pytest

from calculator.calculator import Calculator

@pytest.fixture
def clear_history():
    Calculator.clear_history()

def test_calculator_add(clear_history):
    assert Calculator.add_number(7,3) == 10
    assert Calculator.add_number(6, 6) == 12
    assert Calculator.add_number(7, 7) == 14
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)

def test_clear_history(clear_history):
    assert Calculator.add_number(7,3) == 10
    assert Calculator.add_number(6, 6) == 12
    assert Calculator.add_number(7, 7) == 14
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.clear_history() == True
    assert Calculator.history_count() == 0

def test_count_history(clear_history):
    assert Calculator.history_count() == 0
    assert Calculator.add_number(8, 8) == 16
    assert Calculator.add_number(9, 9) == 18
    assert Calculator.history_count() == 2

def test_get_last_calculation_result(clear_history):
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_last_calculation_added_to_history() == 5

def test_get_first_calculation_result(clear_history):
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_first_calculation_added_to_history() == 4

def test_calculator_subtract(clear_history):
    assert Calculator.subtract_number(1, 2) == -1

def test_calculator_multiply(clear_history):
    assert Calculator.multiply_numbers(1,2) == 2

def test_calculator_division(clear_history):
    assert Calculator.divide_numbers(6,3) == 2
