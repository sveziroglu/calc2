"""Testing the Calculator"""
import pytest
import pandas as pd

from calc.history.calculations import Calculations
from calc.temp.division import Division
from calc.temp.addition import Addition
from calc.temp.multiplication import Multiplication
from calc.subtraction import Subtraction

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    csv_reader = pd.read_csv("files/addition.csv")
    for index, row in csv_reader.iterrows():
        values = (row.value1, row.value2)
        addition = Addition.create(values)
        addition_result = csv_reader["result"][index]
        assert addition.get_result() == addition_result

def test_calculator_subtract_static(clear_history_fixture):
    csv_reader = pd.read_csv("files/subtraction.csv")
    for index, row in csv_reader.iterrows():
        values = (row.value_a, row.value_b)
        subtraction = Subtraction.create(values)
        subtraction_result = csv_reader["result"][index]
        assert subtraction.get_result() == subtraction_result

def test_calculator_multiply_static(clear_history_fixture):
    csv_reader = pd.read_csv("files/multiplication.csv")
    for index, row in csv_reader.iterrows():
        values = (row.value_a, row.value_b)
        multiplication = Multiplication.create(values)
        multiplication_result = csv_reader["result"][index]
        assert multiplication.get_result() == multiplication_result

def test_calculator_divide_static(clear_history_fixture, self=None):
    csv_reader = pd.read_csv("files/division.csv")
    for index, row in csv_reader.iterrows():
        values = (row.value3, row.value4)
        division_result = Division.create(values)
        addition_result = csv_reader["result"][index]
        assert Division.get_result(self) == division_result

