"""This is the calculator"""
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division

#This is how the calculator will solve
class Calculator:
    """This is a calculator class"""
    history = []
    @staticmethod
    def get_history():
        """pulls history of calculator"""
        return Calculator.history
    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """pulls result from last calculation"""
        return Calculator.history[-1].get_result()
    #returns calculator back to 0
    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """Result of first calculation to history"""
        return Calculator.history[0].get_result()
    @staticmethod
    def add_calculation_to_history(calculation):
        """adds calculation to history"""
        Calculator.history.append(calculation)
        #returns calculator to 0
        return True
    @staticmethod
    def get_last_calculation_result_added_to_history():
        """pulls most recent calculation"""
        return Calculator.history[-1].get_result()
    @staticmethod
    def clear_history():
        """Clears history"""
        Calculator.history.clear()
        #return calculator to 0
        return True
    @staticmethod
    def history_count():
        """Counts how much history"""
        return len(Calculator.history)
    @staticmethod
    def add_number(value_a, value_b):
        """Adds number"""
        addition = Addition.create(value_a,value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def subtract_number(value_a, value_b):
        """subtract number"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def multiply_numbers(value_a, value_b):
        """multiply numbers"""
        Calculator.add_calculation_to_history(Multiplication.create(value_a,value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def divide_numbers(value_a, value_b):
        """divide numbers"""
        division = Division.create(value_a, value_b)
        Calculator.add_calculation_to_history(division)
        return Calculator.get_result_of_last_calculation_added_to_history()
