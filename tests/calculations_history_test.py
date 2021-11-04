"""Testing the Calculator"""
import pytest
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()

def test_add_calculation_to_history(clear_history_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    values = (1,2,3,4)
    addition = Addition(values)
    Calculations.add_calculation(addition)
    assert len(Calculations.history) == 1

def test_clear_calculation_history(clear_history_fixture):
    values = (1,2)
    addition = Addition(values)
    Calculations.add_calculation(addition)
    assert len(Calculations.history) == 1
    Calculations.clear_history()
    assert len(Calculations.history) == 0
    assert Calculations.clear_history() == True

def test_get_calculation(clear_history_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    values = (1,2)
    addition = Addition(values)
    Calculations.add_calculation(addition)
    assert Calculations.get_calculation(0).get_result() == 3

def test_get_calculation_last(clear_history_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    values = (1,2)
    addition = Addition(values)
    Calculations.add_calculation(addition)
    assert Calculations.get_last_calculation().get_result() == 3
