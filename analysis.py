# analysis.py
# For the project this program should: 
#   1. Output a summary of each variable to a single text file
#   2. Saves a histogram of each variable to png files
#	3. Outputs a scatter plot of each pair of variables
#   Performs any other analysis you think is appropriate

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# fetching data from csv file

df = pd.read_csv('iris_data.csv')
