"""This is how you extend the Addition class with the Calculation"""
from calc.calculation import Calculation

class Addition(Calculation):
    """The addition class gets the result of the
     calculation A and B come from the parent class"""
    def get_result(self):
        """This will show result"""
        return sum(self.values)
