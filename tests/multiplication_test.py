"""Testing Addition"""
from calc.calculations.multiplication import Multiplication

def test_addition():
    """testing calc result is 0"""
    assert Multiplication.multiply(1,2) == 2
