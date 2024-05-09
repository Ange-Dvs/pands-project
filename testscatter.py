import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_scatter_all(x_variable, y_variable):
    plt.scatter(setosa_df[x_variable], setosa_df[y_variable], color='violet')
    plt.scatter(versicolor_df[x_variable], versicolor_df[y_variable], color='navy')
    plt.scatter(virginica_df[x_variable], virginica_df[y_variable], color='orange')
    plt.xlabel(x_variable) # setting label for x axis 
    plt.ylabel(y_variable) # setting label for x axis 


# fetching data from csv file
df = pd.read_csv('iris_data.csv')

# Filtering the dataset based on class to be able to differeniate in plots later in the program
setosa_df = df[df['class'] == 'Iris-setosa']
versicolor_df = df[df['class'] == 'Iris-versicolor']
virginica_df = df[df['class'] == 'Iris-virginica']

# Define dictionary of variables to plot for histograms and filenames for histogram pngs
x_variables_y_variables = {
    'petal length (cm)': 'petal width (cm)',
    'petal width (cm)': 'sepal length (cm)',
    'petal width (cm)': 'sepal width (cm)',
    'petal width (cm)': 'petal length (cm)',
    'sepal length (cm)': 'sepal width (cm)',
    'sepal length (cm)': 'petal length (cm)',
    'sepal length (cm)': 'petal width (cm)',
    'sepal width (cm)': 'sepal length (cm)',
    'sepal width (cm)': 'petal length (cm)',
    'sepal width (cm)': 'petal width (cm)',
    'petal length (cm)': 'sepal length (cm)',
    'petal length (cm)': 'sepal width (cm)',
    }

# Iterate over variables and filenames
for i, (x_variable, y_variable) in enumerate(x_variables_y_variables.items(), start=1): # issue with this because we will want extra subplots for the titles maybe add blank entries in dictionary if it doesn't cause an issue. 
       create_scatter_all(x_variable, y_variable)
       plt.savefig(f'test{i}.png')
       plt.clf()