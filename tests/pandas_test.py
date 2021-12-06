import pandas as pd
import os
from fileutilities.absolutepath import absolutepath

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
data = pd.read_csv(absolutepath("tests/files/addition.csv"))

print(data)