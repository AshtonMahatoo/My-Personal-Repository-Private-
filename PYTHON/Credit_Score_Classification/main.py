# Pandas is used for working with data sets
import pandas as pd 

# numpy is a Python object used for storing data. 
# The main advantage of NumPy over other Python data structures, 
# such as Python's lists or pandas' Seriesis speed at scale. 
# It's most useful when you're creating large matrices with billions of data points.
import numpy as np  


import csv 
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio 
pio.templates.default = "plotly_white"


data = pd.read_csv("train.csv")
"""
print(data)

print("=====================")

print(data.info())

print("=====================")

print(data.isnull().sum())

print("=====================")
"""

"""
with open('train.csv',"r", newline = "") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    for row in reader:
        print(row)
"""

print(data["Credit_Score"].value_counts())