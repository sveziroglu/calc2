"""Testing Addition"""
from calc.calculations.addition import Addition

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    addition = Addition(1.0,2.0)
    #Act
    #Assert
    assert addition.getResult() == 3.0