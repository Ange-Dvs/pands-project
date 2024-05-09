import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_scatter_all(x_variable, y_variable):
    if i == 1 or i == 6 or i == 11 or i == 16:
        plt.subplot(4,4,i)
        plt.yticks([])
        plt.xticks([])
        plt.plot()
        if i == 1:
            plt.figtext(.16, .82, 'Sepal\nLength', ha='center', fontsize=22, fontstyle='italic')
            #plt.figtext(.50, .50, 'Sepal\nLength', ha='center', fontsize=22, fontstyle='italic')
        elif i == 6:
            plt.figtext(.39, .59, 'Sepal\nWidth', ha='center', fontsize=22, fontstyle='italic')
            #plt.figtext(.50, .50, 'Sepal\nWidth', ha='center', fontsize=22, fontstyle='italic')
        elif i == 11:
            plt.figtext(.63, .35, 'Petal\nLength', ha='center', fontsize=22, fontstyle='italic')
            #plt.figtext(.50, .50, 'Petal\nLength', ha='center', fontsize=22, fontstyle='italic')
        elif i == 16:
            plt.figtext(.86, .12, 'Petal\nWidth', ha='center', fontsize=22, fontstyle='italic')
            #plt.figtext(.50, .50, 'Petal\nLength', ha='center', fontsize=22, fontstyle='italic')
    else:
        plt.subplot(4,4,i)
        plt.scatter(setosa_df[x_variable], setosa_df[y_variable], color='violet')
        plt.scatter(versicolor_df[x_variable], versicolor_df[y_variable], color='navy')
        plt.scatter(virginica_df[x_variable], virginica_df[y_variable], color='orange')
        if i == 3 or i == 7 or i == 8 or i == 9 or i == 10 or i == 14:
            plt.yticks([])
            plt.xticks([])
        elif i == 2:
            plt.yticks([])
            plt.tick_params(axis='x', direction='out', top=True, labeltop=True, bottom=False, labelbottom=False)
        elif i == 4: 
            plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False, labelleft=False)
            plt.tick_params(axis='x', direction='out', top=True, labeltop=True, bottom=False, labelbottom=False)
        elif i == 5:
            plt.xticks([])
        elif i == 12:
            plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False, labelleft=False)
            plt.xlabel(x_variable) # setting label for x axis 
        elif i == 15:
            plt.yticks([])
        
#       plt.xlabel(x_variable) # setting label for x axis 
#       plt.ylabel(y_variable) # setting label for x axis 

# fetching data from csv file
df = pd.read_csv('iris_data.csv')

# Filtering the dataset based on class to be able to differeniate in plots later in the program
setosa_df = df[df['class'] == 'Iris-setosa']
versicolor_df = df[df['class'] == 'Iris-versicolor']
virginica_df = df[df['class'] == 'Iris-virginica']

# Define lsit of variables to plot for x axis value and y axis value for scatter plot pngs
x_variables_y_variables = [('',''),
    ('sepal width (cm)', 'sepal length (cm)'),
    ('petal length (cm)', 'sepal length (cm)'),
    ('petal width (cm)', 'sepal length (cm)'),
    ('sepal length (cm)', 'sepal width (cm)'),
    ('',''),
    ('petal length (cm)', 'sepal width (cm)'),
    ('petal width (cm)', 'sepal width (cm)'),
    ('sepal length (cm)','petal length (cm)'),
    ('sepal width (cm)', 'petal length (cm)'),
    ('',''),
    ('petal width (cm)', 'petal length (cm)'),
    ('sepal length (cm)', 'petal width (cm)'),
    ('sepal width (cm)', 'petal width (cm)'),
    ('petal length (cm)','petal width (cm)'),
    ('','')
]
# Iterate over variables and filenames
plt.figure(figsize=(9, 9)) # figure size is set to avoid the plot being overloaded
for i, (x_variable, y_variable) in enumerate(x_variables_y_variables, start=1):
       create_scatter_all(x_variable, y_variable)

plt.savefig(f'testscatter.png')
