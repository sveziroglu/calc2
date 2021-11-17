"""This is our calculation base class / Abstract Class"""
class Calculation:
    # pylint: disable=too-few-public-methods

    """contstructor - first function called when an object of the class is instantiated"""
    def __init__(self,value_a, value_b):
        #self references the instantiated object of the class
        #instance properties- shared with the child classes
        self.value_a = value_a
        """this self reference is for value_b"""
        self.value_b = value_b
    #Class Factory Method - bound to the class and not the instance of the class
    @classmethod
    def create(cls, value_a, value_b):
        """this is the result"""
        return cls(value_a,value_b)
