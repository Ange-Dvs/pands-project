# analysis.py
# For the project this program should: 
#   1. Output a summary of each variable to a single text file
#   2. Saves a histogram of each variable to png files > Done
#	3. Outputs a scatter plot of each pair of variables > Done (could be improved)
#   Performs any other analysis you think is appropriate

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# fetching data from csv file
df = pd.read_csv('iris_data.csv')

# Filtering the dataset based on class to be able to differeniate in plots later in the program
setosa_df = df[df['class'] == 'Iris-setosa']
versicolor_df = df[df['class'] == 'Iris-versicolor']
virginica_df = df[df['class'] == 'Iris-virginica']
'''
# Creating histogram for sepal length	

plt.hist(df["sepal length (cm)"])
plt.xlabel('Sepal length (cm)') # setting label for x axis 
plt.title("Distribution of sepal length") # setting plot title
plt.savefig("1_sepal_length_hist.png") # saving histogram as PNG file
plt.clf() # clears the current plot to allow a fresh plot for the next histogram to be created

# Creating histogram for sepal width	

plt.hist(df["sepal width (cm)"])
plt.xlabel('Sepal width (cm)') # setting label for x axis 
plt.title("Distribution of sepal width") # setting plot title
plt.savefig("2_sepal_width_hist.png") # saving histogram as PNG file
plt.clf() # clears the current plot to allow a fresh plot for the next histogram to be created

# Creating histogram for petal length	

plt.hist(df["petal length (cm)"])
plt.xlabel('Petal length (cm)') # setting label for x axis 
plt.title("Distribution of petal length (cm)") # setting plot title
plt.savefig("3_petal_length_hist.png") # saving histogram as PNG file
plt.clf() # clears the current plot to allow a fresh plot for the next histogram to be created

# Creating histogram for petal width

plt.hist(df["petal width (cm)"])
plt.xlabel('Petal width (cm)') # setting label for x axis 
plt.title("Distribution of petal width (cm)") # setting plot title
plt.savefig("4_petal_width_hist.png") # saving histogram as PNG file
plt.clf() # clears the current plot to allow a fresh plot for the next histogram to be created
'''
#############################
# Creating a scatter plot showing each pair of variables 
# Setting variables for comparison across the classes  which will be used for the subplots
setosa_sepal_length = setosa_df['sepal length (cm)']
setosa_sepal_width = setosa_df['sepal width (cm)']
setosa_petal_length = setosa_df['petal length (cm)']
setosa_petal_width = setosa_df['petal width (cm)']

versicolor_sepal_length = versicolor_df['sepal length (cm)']
versicolor_sepal_width = versicolor_df['sepal width (cm)']
versicolor_petal_length = versicolor_df['petal length (cm)']
versicolor_petal_width = versicolor_df['petal width (cm)']

virginica_sepal_length = virginica_df['sepal length (cm)']
virginica_sepal_width = virginica_df['sepal width (cm)']
virginica_petal_length = virginica_df['petal length (cm)']
virginica_petal_width = virginica_df['petal width (cm)']

# Creating the .png file for the scatter plot containing the sub-plots of the each variable compared 

plt.subplot(2, 3, 1)  # Creating a subplot for sepal length vs sepal width
# Plotting the 3 species to the plot as different colours
plt.scatter(setosa_sepal_length, setosa_sepal_width, color='purple', label='Setosa', marker = '.')
plt.scatter(versicolor_sepal_length, versicolor_sepal_width, color='orange', label='Versicolor', marker='.')
plt.scatter(virginica_sepal_length, virginica_sepal_width, color='blue', label='Virginica', marker='.')
# Set labels and title
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
#plt.legend()

plt.subplot(2, 3, 2)  # Creating a subplot for sepal length vs petal length
plt.scatter(setosa_sepal_length, setosa_petal_length, color='purple', marker = '.')
plt.scatter(versicolor_sepal_length, versicolor_petal_length, color='orange', marker='.')
plt.scatter(virginica_sepal_length, virginica_petal_length, color='blue', marker='.')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

plt.subplot(2, 3, 3)  # Creating a subplot for sepal length vs petal width
plt.scatter(setosa_sepal_length, setosa_petal_width, color='purple', marker = '.')
plt.scatter(versicolor_sepal_length, versicolor_petal_width,color='orange', marker='.')
plt.scatter(virginica_sepal_length, virginica_petal_width, color='blue', marker='.')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Width (cm)')

plt.subplot(2, 3, 4) # Creating plot for sepal width vs petal length
plt.scatter(setosa_sepal_width, setosa_petal_length, color='purple', marker = ".")
plt.scatter(versicolor_sepal_width, versicolor_petal_length, color='orange', marker = ".")
plt.scatter(virginica_sepal_width, virginica_petal_length, color='blue', marker = ".")
plt.xlabel('Sepal width (cm)')
plt.ylabel('Petal Length (cm)')

plt.subplot(2, 3, 5) # Creating plot for sepal width vs petal width
plt.scatter(setosa_sepal_width, setosa_petal_width, color='purple', marker = '.')
plt.scatter(versicolor_sepal_width, versicolor_petal_width, color='orange', marker='.')
plt.scatter(virginica_sepal_width, virginica_petal_width, color='blue', marker='.')
plt.xlabel('Sepal width (cm)')
plt.ylabel('Petal width (cm)')

plt.subplot(2, 3, 6) # Creating plot for petal length vs petal width
plt.scatter(setosa_petal_length, setosa_petal_width, color='purple', marker = '.')
plt.scatter(versicolor_petal_length, versicolor_petal_width, color='orange', marker='.')
plt.scatter(virginica_petal_length, virginica_petal_width, color='blue', marker='.')
plt.xlabel('Petal length (cm)')
plt.ylabel('Petal width (cm)')
plt.suptitle('Iris Data variables compared', fontsize=18, va = 'top')
plt.figlegend(loc = "upper right", ncols = 3, bbox_to_anchor=(.75, .95), fontsize=10) # creating one legend for the subplots and setting it's location to the top center for the plot


plt.tight_layout()  # Adjust the layout of subplots to prevent overlapping
plt.savefig("5_all_variables_scatter.png") # saving scatter plot as PNG file