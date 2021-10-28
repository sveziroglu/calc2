"""Testing Addition"""
from calc.calculations.subtraction import Subtraction

def test_subtraction():
    """testing calc result is -1"""
    assert Subtraction.subtract(1,2) == -1
