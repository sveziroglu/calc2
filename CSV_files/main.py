import pandas as pd
import numpy as np
import time
import glob
import pathlib



from calculator.calculator import *
from calc.calculations.calculation import Calculation
from calc.history.calculations import Calculations
df_addition = pd.read_csv("../tests/files/addition.csv")
df_subtraction = pd.read_csv("../tests/files/subtraction.csv")
df_mulitplication = pd.read_csv("../tests/files/multiplication.csv")
df_division = pd.read_csv("../tests/files/division.csv")

df_logs = pd.read_csv("../tests/log_files/log.csv")
df_excep_logs = pd.read_csv("../tests/log_files/exception_log.csv")
mainCalculator=Calculator()

columns = list(df_logs)
excep_columns = list(df_logs)
print(columns)
recordNum = 0
data = []
log_data = []

print("---------------Computing Addition CSV------------")
for index, row in df_addition.iterrows():
    value_a = row.value1
    value_b = row.value2
    addResult = mainCalculator.add_number(value_a,value_b)
    values = [recordNum,time.time(), "addition.csv", addResult]
    recordNum += 1
    zipped = zip(columns, values)
    a_dictionary = dict(zipped)
    print(a_dictionary)
    data.append(a_dictionary)



print(data)

print(" ---------------Completed Computing Addition CSV------------")

print("---------------Computing Subtraction CSV------------")
for index, row in df_subtraction.iterrows():
    Result = mainCalculator.subtract_number(row.value_a,row.value_b)
    values = [recordNum,time.time(), "subtraction.csv", Result]
    recordNum += 1
    zipped = zip(columns, values)
    a_dictionary = dict(zipped)
    print(a_dictionary)
    data.append(a_dictionary)

print(data)

print(" ---------------Completed Computing Subtraction CSV------------")

print("---------------Computing Multiplication CSV------------")
for index, row in df_mulitplication.iterrows():
    addResult = mainCalculator.multiply_numbers(row['value_a'], row['value_b'])
    values = [recordNum,time.time(), "multiplication.csv", addResult]
    recordNum += 1
    zipped = zip(columns, values)
    a_dictionary = dict(zipped)
    print(a_dictionary)
    data.append(a_dictionary)

print(data)

print(" ---------------Completed Computing Multiplication CSV------------")

print("---------------Computing Division CSV------------")
for index, row in df_division.iterrows():
    value_a = row.value1
    value_b = row.value2
    Result = mainCalculator.divide_numbers(value_a,value_b)
    values = [recordNum,time.time(), "division.csv", Result]
    recordNum += 1
    zipped = zip(columns, values)
    a_dictionary = dict(zipped)
    print(a_dictionary)
    data.append(a_dictionary)

print(data)

print(" ---------------Completed Computing Division CSV------------")


#exception for division
for index, row in df_division.iterrows():
    value_a = row.value_a
    value_b = row.value_b
    try:
        Result = mainCalculator.subtract_number(value_a,value_b)
    except ZeroDivisionError:
        values = [recordNum, "ZeroDivisionError", "division.csv"]
        recordNum += 1
        zipped = zip(excep_columns, values)
        a_dictionary = dict(zipped)
        print(a_dictionary)
        log_data.append(a_dictionary)
        continue

    values = [recordNum,time.time(), "division.csv",Result]
    recordNum += 1
    zipped = zip(columns, values)
    a_dictionary = dict(zipped)
    print(a_dictionary)
    data.append(a_dictionary)


df_excep_logs = df_excep_logs.append(log_data,True)
df_logs = df_logs.append(data,True)
print(df_logs)
df_logs.to_csv('../tests/log_files/log.csv')

