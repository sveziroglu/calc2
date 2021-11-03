"""Calculation Class"""
import pprint


class Calculation:


    def __init__(self,values: tuple):
        self.values = Calculation.convert_args_to_list_float(values)

    @staticmethod
    def convert_args_to_list_float(values):
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float
