"""Testing Subtraction"""
from calc.calculations.subtraction import Subtraction

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    subtraction = Subtraction(1,2)
    #Act
    #Assert
    assert subtraction.getResult() == -1