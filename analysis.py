# analysis.py
# For the project this program should: 
#   1. Output a summary of each variable to a single text file > Started
#   2. Saves a histogram of each variable to png files > Done
#	3. Outputs a scatter plot of each pair of variables > Done
#   Performs any other analysis you think is appropriate

import pandas as pd
import numpy
import matplotlib.pyplot as plt
import os

# Setting filename for text file
FILENAME = 'IRIS_Summary.txt'

def check_png_file_exists(PNG_filenames):
    if os.path.exists(PNG_filenames):
        raise FileExistsError

def write_summary_file(FILENAME): # creating a function which will create the text file when called.
        try:
                with open(FILENAME, 'x') as f: # "x" creates the new text file and the FILENAME variable defined in the main code is used to name the file.
                        f.write(str(intro)) # writing as .txt means the answer must be cast to a string to store
                        f.write(str(num_values)) # writing as .txt means the answer must be cast to a string to store
                        
                        count_class = df["class"].value_counts() # getting the count of the male and female entries in the dataset
                        f.write(str(count_class))
                        print (f'\nSummary {FILENAME} created.\n')
        except FileExistsError:
                print (f'\nError: Filename {FILENAME} already exists in folder.\n')

def create_histograms(PNG_filenames, variable_to_plot): # creating histogram of sepal length
    # Creating histogram for sepal length not deferentiating per species
        try: 
                check_png_file_exists(PNG_filenames)
                plt.figure(figsize=(10,5))
                plt.subplot(1, 2, 1)
                plt.hist(df[variable_to_plot])
                plt.title('All classes of Iris together')
                #plt.savefig("sepal_length_hist.png")

                plt.subplot(1, 2, 2)
                # Concatenate the petal width data from all three species
                all_sepal_lengths = [setosa_df[variable_to_plot], versicolor_df[variable_to_plot], virginica_df[variable_to_plot]]

                # Plotting a histogram
                plt.hist(all_sepal_lengths,
                        bins=10,
                        stacked=True,
                        label=['Setosa', 'Versicolor', 'Virginica'],
                        edgecolor='white',
                        color=['violet', 'navy', 'orange'])
                plt.title('Colour coded per class of Iris')
                plt.yticks([])

                plt.tight_layout()
                plt.legend()

                plt.suptitle(f'Distribution of {variable_to_plot}',  fontsize = 18, y= 1.05) # setting the title for the subplots
                # Adding a super x label to replace having two separate labels for the x axis
                plt.figtext(0.5, -0.01, f'{variable_to_plot}', ha='center', fontsize=12, fontstyle='italic')

                plt.savefig(PNG_filenames, bbox_inches='tight') # saving scatter plotas PNG file with bbox_inches set to tight to adjust the title
                plt.clf() # clears the current plot to allow a fresh plot for the next histogram to be created

                print(f'Histogram {PNG_filenames} created.\n')

        except FileExistsError:
                #print(f'The file {PNG_filenames} already exists.')
                print(f'Error: Filename {PNG_filenames} already exists in folder. \n')

def scatter_all_variables(PNG_filenames):
    # Creating a scatter plot showing each pair of variables 
    # Creating the .png file for the scatter plot containing the sub-plots of the each variable compared 
        try: 
                check_png_file_exists(PNG_filenames)
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
                plt.savefig(PNG_filenames, bbox_inches='tight') # saving scatter plot as PNG file with bbox_inches set to tight to adjust the title
                print(f'Scatter plot {PNG_filenames} created.\n')
        
        except FileExistsError:
                print(f'Error: Filename {PNG_filenames} already exists in folder.\n')

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

# Define dictionary of variables to plot for histograms and filenames for histogram pngs
variables_and_filenames = {
    'sepal length (cm)': '1_sepal_length_hist.png',
    'sepal width (cm)': '2_sepal_width_hist.png',
    'petal length (cm)': '3_petal_length_hist.png',
    'petal width (cm)': '4_petal_width_hist.png'}

write_summary_file(FILENAME)
 
# Iterate over variables and filenames
for i, (variable_to_plot, PNG_filenames) in enumerate(variables_and_filenames.items()):
       create_histograms(PNG_filenames, variable_to_plot)

PNG_filenames = '5_all_variables_scatter.png' # updates the PNG_filenames value so that the error catching function can be reused for the scatter plot.

scatter_all_variables(PNG_filenames)