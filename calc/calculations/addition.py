"""Addition Class"""

class Addition:

    # default constructor
    def __init__(self,value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    def getResult(self):
        return self.value_a + self.value_b
