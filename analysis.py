# analysis.py
# For the project this program should: 
#   1. Output a summary of each variable to a single text file > Started
#   2. Saves a histogram of each variable to png files > Done
#	3. Outputs a scatter plot of each pair of variables > Done
#   Performs any other analysis you think is appropriate

import pandas as pd
import numpy
import matplotlib.pyplot as plt

# Setting filename for text file
FILENAME = 'IRIS_Summary.txt'

def write_summary_file(): # creating a function which will create the text file when called.
    with open(FILENAME, 'a') as f: # opens the file assigned to the FILENAME variable in append mode for text files "a"
        f.write(str(intro)) # writing as .txt means the answer must be cast to a string to store
        f.write(str(num_values)) # writing as .txt means the answer must be cast to a string to store
        
        count_class = df["class"].value_counts() # getting the count of the male and female entries in the dataset
        f.write(str(count_class))

def create_histograms(): # creating histograms of individual variables
    # Creating histogram for sepal length	
    plt.figure(figsize=(10,5))
    plt.subplot(1, 2, 1)
    plt.hist(df["sepal length (cm)"], label= 'All\n types')
    plt.xlabel('Sepal length (cm)') # setting label for x axis 
    plt.title("Distribution of sepal length") # setting plot title
    plt.legend()
    #plt.savefig("sepal_length_hist.png")

    plt.subplot(1, 2, 2)
    # Concatenate the petal width data from all three species
    all_sepal_lengths = [setosa_df['sepal length (cm)'], versicolor_df['sepal length (cm)'], virginica_df['sepal length (cm)']]

    # Plotting a histogram
    plt.hist(all_sepal_lengths,
            bins=10,
            stacked=True,
            label=['Setosa', 'Versicolor', 'Virginica'],
            edgecolor='white',
            color=['violet', 'navy', 'orange'])
    plt.title("Distribution of sepal length per species of Iris") # setting plot title
    plt.tight_layout()
    plt.legend()
    plt.savefig("1_sepal_length_hist.png") # saving histogram as PNG file
    plt.clf() # clears the current plot to allow a fresh plot for the next histogram to be created

    # Creating histogram for sepal width	
    plt.figure(figsize=(10,5))
    plt.subplot(1, 2, 1)
    plt.hist(df["sepal width (cm)"], label= 'All\n types')
    plt.xlabel('Sepal width (cm)') # setting label for x axis 
    plt.title("Distribution of sepal width") # setting plot title
    plt.legend()
    #plt.savefig("sepal_length_hist.png")

    plt.subplot(1, 2, 2)
    # Concatenate the petal width data from all three species
    all_sepal_widths = [setosa_df['sepal width (cm)'], versicolor_df['sepal width (cm)'], virginica_df['sepal width (cm)']]

    # Plotting a histogram
    plt.hist(all_sepal_widths,
            bins=10,
            stacked=True,
            label=['Setosa', 'Versicolor', 'Virginica'],
            edgecolor='white',
            color=['violet', 'navy', 'orange'])
    plt.title("Distribution of sepal width per species of Iris") # setting plot title
    plt.tight_layout()
    plt.legend()
    plt.savefig("2_sepal_width_hist.png") # saving histogram as PNG file
    plt.clf() # clears the current plot to allow a fresh plot for the next histogram to be created

    # Creating histogram for petal length

    plt.figure(figsize=(10,5))
    plt.subplot(1, 2, 1)
    plt.hist(df["petal length (cm)"], label= 'All\n types')
    plt.xlabel('Petal length (cm)') # setting label for x axis 
    plt.title("Distribution of petal length (cm)") # setting plot title
    plt.legend()
    #plt.savefig("sepal_length_hist.png")

    plt.subplot(1, 2, 2)
    # Concatenate the petal width data from all three species
    all_petal_lengths = [setosa_df['petal length (cm)'], versicolor_df['petal length (cm)'], virginica_df['petal length (cm)']]
    plt.hist(all_petal_lengths,
            bins=10,
            stacked=True,
            label=['Setosa', 'Versicolor', 'Virginica'],
            edgecolor='white',
            color=['violet', 'navy', 'orange'])
    plt.title("Distribution of petal length per species of Iris") # setting plot title
    plt.tight_layout()
    plt.legend()
    plt.savefig("3_petal_length_hist.png")
    plt.clf() # clears the current plot to allow a fresh plot for the next histogram to be created

    # Creating histogram for petal width
    plt.figure(figsize=(10,5))
    plt.subplot(1, 2, 1)
    plt.hist(df["petal width (cm)"], label= 'All\n types')
    plt.xlabel('Petal width (cm)') # setting label for x axis 
    plt.title("Distribution of petal width (cm)") # setting plot title
    # plt.savefig("petal_width_hist.png")
    plt.legend()
    #plt.savefig("sepal_length_hist.png")

    plt.subplot(1, 2, 2)
    # Concatenate the petal width data from all three species
    all_petal_widths = [setosa_df['petal width (cm)'], versicolor_df['petal width (cm)'], virginica_df['petal width (cm)']]

    # Plotting a histogram
    plt.hist(all_petal_widths,
            bins=10,
            stacked=True,
            label=['Setosa', 'Versicolor', 'Virginica'],
            edgecolor='white',
            color=['violet', 'navy', 'orange'])
    plt.title("Distribution of petal width per species of Iris") # setting plot title
    plt.tight_layout()
    plt.legend()
    plt.savefig("4_petal_width_hist.png")

def scatter_all_variables():
    # Creating a scatter plot showing each pair of variables 
    # Creating the .png file for the scatter plot containing the sub-plots of the each variable compared 
    # Setting variables for comparison across the species which will be used for the subplots
    # sepal length vs sepal width, sepal length vs petal length, sepal length vs petal width
    # sepal width vs petal length, sepal width vs petal width
    # petal length vs petal width
    # petal width
    # Setting variables for comparison across the species which will be used for the subplots
    # sepal length vs sepal width, sepal length vs petal length, sepal length vs petal width
    # sepal width vs petal length, sepal width vs petal width
    # petal length vs petal width
    # petal width
    plt.figure(figsize=(9, 9))
    plt.subplots_adjust(top=1)

    plt.subplot(4, 4, 1) 
    plt.figtext(.16, .82, 'Sepal\nLength', ha='center', fontsize=22, fontstyle='italic')
    plt.yticks([])
    plt.xticks([])

    plt.subplot(4, 4, 2)  # Creating a subplot for sepal width and sepal length
    plt.scatter(setosa_sepal_width, setosa_sepal_length, color='violet', label='Setosa')
    plt.scatter(versicolor_sepal_width, versicolor_sepal_length, color='navy', label='Versicolor')
    plt.scatter(virginica_sepal_width, virginica_sepal_length, color='orange', label='Virginica')
    plt.tick_params(axis='x', direction='out', top=True, labeltop=True, bottom=False, labelbottom=False)
    plt.yticks([])

    plt.subplot(4, 4, 3)  # Creating a subplot for sepal length vs petal width
    plt.scatter(setosa_petal_length, setosa_sepal_length, color='violet')
    plt.scatter(versicolor_petal_length, versicolor_sepal_length, color='navy')
    plt.scatter(virginica_petal_length, virginica_sepal_length, color='orange')
    plt.yticks([])
    plt.xticks([])

    plt.subplot(4, 4, 4) # Creating plot for sepal width vs petal length
    plt.scatter(setosa_petal_width, setosa_sepal_length, color='violet')
    plt.scatter(versicolor_petal_width, versicolor_sepal_length, color='navy')
    plt.scatter(virginica_petal_width, virginica_sepal_length, color='orange')
    plt.tick_params(axis='x', direction='out', top=True, labeltop=True, bottom=False, labelbottom=False)
    plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False, labelleft=False)

    plt.subplot(4, 4, 5) # Creating plot for sepal width vs petal width
    plt.scatter(setosa_sepal_length, setosa_sepal_width, color='violet')
    plt.scatter(versicolor_sepal_length, versicolor_sepal_width, color='navy')
    plt.scatter(virginica_sepal_length, virginica_sepal_width, color='orange')
    plt.xticks([])

    plt.subplot(4, 4, 6) # Creating plot for petal length vs petal width
    plt.figtext(.39, .59, 'Sepal\nWidth', ha='center', fontsize=22, fontstyle='italic')
    plt.yticks([])
    plt.xticks([])

    plt.subplot(4, 4, 7)
    plt.scatter( setosa_petal_length, setosa_sepal_width, color='violet')
    plt.scatter( versicolor_petal_length, versicolor_sepal_width, color='navy')
    plt.scatter( virginica_petal_length, virginica_sepal_width, color='orange')
    plt.yticks([])
    plt.xticks([])

    plt.subplot(4, 4, 8)
    plt.scatter(setosa_petal_width, setosa_sepal_width, color='violet')
    plt.scatter(versicolor_petal_width, versicolor_sepal_width, color='navy')
    plt.scatter(virginica_petal_width, virginica_sepal_width, color='orange')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(4, 4, 9)
    plt.scatter(setosa_sepal_length, setosa_petal_length, color='violet')
    plt.scatter(versicolor_sepal_length, versicolor_petal_length, color='navy')
    plt.scatter(virginica_sepal_length, virginica_petal_length, color='orange')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(4, 4, 10)
    plt.scatter(setosa_sepal_width, setosa_petal_length, color='violet')
    plt.scatter(versicolor_sepal_width, versicolor_petal_length, color='navy')
    plt.scatter(virginica_sepal_width, virginica_petal_length, color='orange')
    plt.yticks([])
    plt.xticks([])

    plt.subplot(4, 4, 11)
    plt.figtext(.63, .35, 'Petal\nLength', ha='center', fontsize=22, fontstyle='italic')
    plt.yticks([])
    plt.xticks([])

    plt.subplot(4, 4, 12)
    plt.scatter(setosa_petal_width, setosa_petal_length, color='violet')
    plt.scatter(versicolor_petal_width, versicolor_petal_length, color='navy')
    plt.scatter(virginica_petal_width, virginica_petal_length, color='orange')
    plt.xticks([])
    plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False, labelleft=False)

    plt.subplot(4, 4, 13)
    plt.scatter(setosa_sepal_length, setosa_petal_width, color='violet')
    plt.scatter(versicolor_sepal_length, versicolor_petal_width, color='navy')
    plt.scatter(virginica_sepal_length, virginica_petal_width, color='orange')

    plt.subplot(4, 4, 14)
    plt.scatter(setosa_sepal_width, setosa_petal_width, color='violet')
    plt.scatter(versicolor_sepal_width, versicolor_petal_width, color='navy')
    plt.scatter(virginica_sepal_width, virginica_petal_width, color='orange')
    plt.yticks([])
    plt.xticks([])

    plt.subplot(4, 4, 15)
    plt.scatter(setosa_petal_length, setosa_petal_width, color='violet')
    plt.scatter(versicolor_petal_length, versicolor_petal_width, color='navy')
    plt.scatter(virginica_petal_length, virginica_petal_width, color='orange')
    plt.yticks([])

    plt.subplot(4, 4, 16) 
    plt.figtext(.86, .12, 'Petal\nWidth', ha='center', fontsize=22, fontstyle='italic')
    plt.yticks([])
    plt.xticks([])

    plt.tight_layout()
    plt.suptitle('All variables', y=1.08, fontsize=32)
    plt.figlegend(loc = "upper center", ncols = 3, bbox_to_anchor=(0.5, 1.04), fontsize=14) # creating one legend for the subplots and setting it's location to the top center for the plot
    plt.savefig("5_all_variables_scatter.png", bbox_inches='tight') # saving scatter plot as PNG file with bbox_inches set to tight to adjust the title

# fetching data from csv file
df = pd.read_csv('iris_data.csv')

# Filtering the dataset based on class to be able to differeniate in plots later in the program
setosa_df = df[df['class'] == 'Iris-setosa']
versicolor_df = df[df['class'] == 'Iris-versicolor']
virginica_df = df[df['class'] == 'Iris-virginica']

# Setting variables for comparison across the classes  which will be used for the subplots
setosa_sepal_length = setosa_df['sepal length (cm)'].to_numpy()
setosa_sepal_width = setosa_df['sepal width (cm)'].to_numpy()
setosa_petal_length = setosa_df['petal length (cm)'].to_numpy()
setosa_petal_width = setosa_df['petal width (cm)'].to_numpy()

versicolor_sepal_length = versicolor_df['sepal length (cm)'].to_numpy()
versicolor_sepal_width = versicolor_df['sepal width (cm)'].to_numpy()
versicolor_petal_length = versicolor_df['petal length (cm)'].to_numpy()
versicolor_petal_width = versicolor_df['petal width (cm)'].to_numpy()

virginica_sepal_length = virginica_df['sepal length (cm)'].to_numpy()
virginica_sepal_width = virginica_df['sepal width (cm)'].to_numpy()
virginica_petal_length = virginica_df['petal length (cm)'].to_numpy()
virginica_petal_width = virginica_df['petal width (cm)'].to_numpy()

# Printing a summary of the numeric valyes of the dataset

num_values = df.describe()
intro = (f'The IRIS dataset, created in 1936, is a popular dataset commonly used for exploring data analysis and data visualisation.\n\nSpecies:\n\tThe dataset consists of measurements for 3 different classes (setosa, versicolor and virginica) of Iris flowers.\nThere are 50 entries per class detailed in the dataset.\nAs the classes variable are plain text, the data type string will be applicable here.\n\nFour characteristics of the flowers were tracked including sepal length (cm), sepal width (cm), petal length (cm) and petal width (cm)\nThese four variables are numeric values and looking at the raw data we can see decimal places are present.\nWith this, the data type used for this variables will be float.\n\n')

write_summary_file()
print('Summary text file has been created.\n')
create_histograms()
print('Histogram pngs have been created\n')
scatter_all_variables()
print('Scatter plot of all variables has been created\n')