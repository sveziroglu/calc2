"""Testing the Calculator"""
import pytest
import pandas as pd

from calc.history.calculations import Calculations
from calc.division import Division
from calc.addition import Addition
from calc.multiplication import Multiplication
from calc.subtraction import Subtraction
from fileutilities.absolutepath import absolutepath

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    csv_reader = pd.read_csv(absolutepath("tests/files/addition.csv"))
    for index, row in csv_reader.iterrows():
        addition = Addition.create(row.value1, row.value2)
        addition_result = csv_reader["result"][index]
        assert addition.get_result() == addition_result

def test_calculator_subtract_static(clear_history_fixture):
    csv_reader = pd.read_csv(absolutepath("tests/files/subtraction.csv"))
    for index, row in csv_reader.iterrows():
        subtraction = Subtraction.create(row.value_a, row.value_b)
        subtraction_result = csv_reader["result"][index]
        assert subtraction.get_result() == subtraction_result

def test_calculator_multiply_static(clear_history_fixture):
    csv_reader = pd.read_csv(absolutepath("tests/files/multiplication.csv"))
    for index, row in csv_reader.iterrows():
        multiplication = Multiplication.create(row.value_a, row.value_b)
        multiplication_result = csv_reader["result"][index]
        assert multiplication.get_result() == multiplication_result

def test_calculator_divide_static(clear_history_fixture):
    csv_reader = pd.read_csv(absolutepath("tests/files/division.csv"))
    for index, row in csv_reader.iterrows():
        division = Division.create(row.value3, row.value4)
        division_result = csv_reader["result"][index]
        assert division.get_result() == division_result

