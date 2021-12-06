import glob
import pathlib
import os
import pandas as pd
import time


from calculator.calculator import Calculator


def process(files):
    for file in files:
        basename = os.path.basename(file)

        if basename == "addition.csv":
            print("add")
            df = pd.read_csv(file)
            results_arr = []
            for index, row in df.iterrows():
                temp = Calculator.add_number(row['value1'], row['value2'])
                with open("logs/results.txt", "a") as fp:
                    fp.write(f"Time: {time.time()}, File: {file}, "
                             f"Record Number: {index}, " f"Operation: add, Result: {temp}\n")
                    fp.close()
                results_arr.append(temp)
            df["result"] = results_arr
            with open(f"outputs/{basename}", "w") as fp:
                df.to_csv(fp)


        if basename == "subtraction.csv":
            print("Processing Subtraction CSV")
            df = pd.read_csv(file)
            results_arr = []
            for index, row in df.iterrows():
                temp = Calculator.subtract_number(row['value1'], row['value2'])
                with open("logs/results.txt", "a") as fp:
                    fp.write(
                        f"Time: {time.time()}, File: {file}, Record Number: {index}, "
                        f"Operation: subtract, Result: {temp}\n")
                    fp.close()
                results_arr.append(temp)
            df["result"] = results_arr
            with open(f"outputs/{basename}", "w") as fp:
                df.to_csv(fp)


        if basename == "multiplication.csv":
            print("multiply")
            df = pd.read_csv(file)
            results_arr = []
            for index, row in df.iterrows():
                temp = Calculator.multiply_numbers(row['value1'], row['value2'])
                with open("logs/results.txt", "a") as fp:
                    fp.write(
                        f"Time: {time.time()}, File: {file}, Record Number: {index}, "
                        f"Operation: multiply, Result: {temp}\n")
                    fp.close()
                results_arr.append(temp)
            df["result"] = results_arr
            with open(f"outputs/{basename}", "w") as fp:
                df.to_csv(fp)


        if basename == "division.csv":
            print("division")
            df = pd.read_csv(file)
            results_arr = []
            # Looping through records
            for index, row in df.iterrows():
                # Catching error
                if row['value2'] == 0:
                    with open("logs/exceptions.txt", "a") as fp:
                        fp.write(f"File: {file}, Record Number: {index}\n")
                        fp.close()
                    results_arr.append("NaN")
                else:
                    # Operation
                    temp = Calculator.divide_numbers(row['value1'], row['value2'])
                    # Write to log
                    with open("logs/results.txt", "a") as fp:
                        fp.write(f"Time: {time.time()}, File: {file}, Record Number: {index}, "
                                 f"Operation: divide, Result: {temp}\n")
                        fp.close()
                    results_arr.append(temp)

            # Creating output CSVs
            df["result"] = results_arr
            with open(f"outputs/{basename}", "w") as fp:
                df.to_csv(fp)

    return 0


def main():
    path = pathlib.Path(__file__).parent / "inputs"
    # print ("path: " + str(path))
    files = glob.glob(str(path) + "/*")
    # print(files)
    files_len = len(files)
    while True:
        if files_len != 0:
            print("Processing...")
            done = process(files)
            files_len = done
        else:
            print("Running...", end="\r")

    return True


main()
