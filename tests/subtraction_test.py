"""Testing Subtraction"""
from calc.subtraction import Subtraction

def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    #Arrange
    subtraction = Subtraction(1.0,2.0)
    #Act
    #Assert
    assert subtraction.get_result() == -1.0
