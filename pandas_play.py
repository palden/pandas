import sys
import os
import pandas

if os.path.exists("temps-today.csv"):
    datum = pandas.read_csv("temps-today.csv")
    print(datum.mean()[0])
else:
    print("File does not exist")
