# analysis.py
# For the project this program should: 
#   1. Output a summary of each variable to a single text file > Started
#   2. Saves a histogram of each variable to png files > Done
#	3. Outputs a scatter plot of each pair of variables > Done
#   Performs any other analysis you think is appropriate

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Setting filename for text file to be reused later in the code.
FILENAME = 'IRIS_Summary.txt'

def check_png_file_exists(PNG_filenames): # creating a function which will check if the PNG files are already existing before trying to create them
    if os.path.exists(PNG_filenames): # using OS library the value set in "PNG_filenames" is used to check if the file is already existing 
        raise FileExistsError # if the file exists the FileExists Error is thrown

def write_summary_file(FILENAME): # creating a function which will create the text file when called.
        try: # first the new text file is attempted to be created 
                with open(FILENAME, 'x') as f: # "x" creates the new text file and the FILENAME variable defined at the beginning of the main code block is used to name the file.
                        f.write(str(intro)) # writing as .txt means the answer must be cast to a string to store
                        f.write(str(num_values)) # writing as .txt means the answer must be cast to a string to store
                        
                        count_class = df["class"].value_counts() # getting the count of the entries in the dataset per class of Iris
                        f.write(str(f'\n\n{count_class}')) # writing the count of the classes to the text file
                        print (f'\nSummary {FILENAME} created.\n') # not to user that the file has been created
        except FileExistsError: # if the file exists when it is attempted to use "x" to create the file then a FileExistsError is thrown
                print (f'\nError: Filename {FILENAME} already exists in folder.\n') # This message will be printed to the user if the FileExistsError is triggered  

def create_histograms(PNG_filenames, variable_to_plot): # creating a function which can be reused to create a histogram of each variable and also to check if the file is already existing
        try: # First this path is attempted to be executed
                check_png_file_exists(PNG_filenames) # the function earlier created to check if the png file exists is triggered. If the file does not exist the code will continue to the next line. If the file does already exist the FileExistsError will be thrown and the code will jump to the except condition.
                plt.figure(figsize=(10,5)) # figure size is set to avoid the plot being overloaded
                plt.subplot(1, 2, 1) # size of subplot is defined with 1 row and 2 columns
                plt.hist(df[variable_to_plot]) # the histogram is created using the value assigned to the variable_to_plot.
                plt.title('All classes of Iris together') # adding the title to the first subplot

                plt.subplot(1, 2, 2) # plotting the subplot to be placed in the second column
                all_sepal_lengths = [setosa_df[variable_to_plot], versicolor_df[variable_to_plot], virginica_df[variable_to_plot]] # using the filtered datasets to select the information per class of Iris to enable colour coding of the histogram per class

                plt.hist(all_sepal_lengths,
                        bins=10, # setting the number of bins
                        stacked=True, # stacked allows us to stack the data into neat columns with the species showing in a towered way 
                        label=['Setosa', 'Versicolor', 'Virginica'], # assigning the labels for the legend
                        edgecolor='white', # setting the colour of the outline of the bins
                        color=['violet', 'navy', 'orange']) # setting the colour of the columns
                plt.title('Colour coded per class of Iris') # adding the title to the second subplot
                plt.yticks([]) # removing y ticks since the same y values are used as shown in the subplot in the first position

                plt.tight_layout() # avoiding any overlap in text or plots in the figure 
                plt.legend() # generating the legend using the labels set

                plt.suptitle(f'Distribution of {variable_to_plot}',  fontsize = 18, y= 1.05) # setting the overall title for the figure
                # Adding a super x label to replace having two separate labels for the x axis
                plt.figtext(0.5, -0.01, f'{variable_to_plot}', ha='center', fontsize=12, fontstyle='italic')

                plt.savefig(PNG_filenames, bbox_inches='tight') # saving scatter plotas PNG file with bbox_inches set to tight to avoid any text or info being cut from the figure
                plt.clf() # clears the current plot to allow a fresh plot for the next histogram to be created

                print(f'Histogram {PNG_filenames} created.\n') # printing the confirmation for a histograms creation 

        except FileExistsError: # If the PNG file is found to already exist when calling check_png_file_exists() function this path is followed
                print(f'Error: Filename {PNG_filenames} already exists in folder. \n') # printing the error that the histogram already exists

def scatter_all_variables(PNG_filenames):
    # Creating a scatter plot showing each pair of variables 
    # Creating the .png file for the scatter plot containing the sub-plots of the each variable compared 
        try: # First this path is attempted to be executed
                check_png_file_exists(PNG_filenames) # the function earlier created to check if the png file exists is triggered. If the file does not exist the code will continue to the next line. If the file does already exist the FileExistsError will be thrown and the code will jump to the except condition.
                plt.figure(figsize=(9, 9)) # figure size is set to avoid the plot being overloaded
                plt.subplot(4, 4, 1)  # plotting the subplot to be placed in the first position. The size of the subplot is also set with 4 rows & columns.
                plt.figtext(.16, .82, 'Sepal\nLength', ha='center', fontsize=22, fontstyle='italic') # creating text to enter in the first subplot. The x & y points are set for the location of the text. The alignment, size and style of the font is set.  
                plt.yticks([]) # y ticks are removed 
                plt.xticks([]) # x ticks are removed 

                plt.subplot(4, 4, 2)  # plotting the subplot to be placed in the second position. The sepal width on x axis vs sepal length on y axis will be reflected in this subplot 
                plt.scatter(setosa_sepal_width, setosa_sepal_length, color='violet', label='Setosa') # variables selected for the sepal width & length for Setosa class, the colour is assigned and the label is set.
                plt.scatter(versicolor_sepal_width, versicolor_sepal_length, color='navy', label='Versicolor') # variables selected for the sepal width & length for Versicolor class, the colour is assigned and the label is set.
                plt.scatter(virginica_sepal_width, virginica_sepal_length, color='orange', label='Virginica') # variables selected for the sepal width & length for Virginica class, the colour is assigned and the label is set.
                plt.tick_params(axis='x', direction='out', top=True, labeltop=True, bottom=False, labelbottom=False) # adjust the location of the ticks on the x axis to be positioned at the top of the plot
                plt.yticks([]) # removing y ticks

                plt.subplot(4, 4, 3)  # plotting the subplot to be placed in the second position. The petal length on x axis vs sepal length on y axis will be reflected in this subplot 
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
                plt.figtext(.39, .59, 'Sepal\nWidth', ha='center', fontsize=22, fontstyle='italic') # creating text to enter in the sixth subplot. The x & y points are set for the location of the text. The alignment, size and style of the font is set.  
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
                plt.figtext(.63, .35, 'Petal\nLength', ha='center', fontsize=22, fontstyle='italic') # creating text to enter in the eleventh subplot. The x & y points are set for the location of the text. The alignment, size and style of the font is set.  
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
                plt.figtext(.86, .12, 'Petal\nWidth', ha='center', fontsize=22, fontstyle='italic') # creating text to enter in the sixteenth subplot. The x & y points are set for the location of the text. The alignment, size and style of the font is set.  
                plt.yticks([])
                plt.xticks([])

                plt.tight_layout() 
                plt.suptitle('All variables', y=1.08, fontsize=32) # adding a title to the figure, setting the location on the y axis and also setting the font size
                plt.figlegend(loc = "upper center", ncols = 3, bbox_to_anchor=(0.5, 1.04), fontsize=14) # creating one legend for the subplots and setting it's location to the top center for the plot and spreading it into 3 columns
                plt.savefig(PNG_filenames, bbox_inches='tight') # saving scatter plot as PNG file with bbox_inches set to tight to adjust to fit the whole figure
                print(f'Scatter plot {PNG_filenames} created.\n') # printing the confirmation for a histograms creation 
        
        except FileExistsError: # If the PNG file is found to already exist when calling check_png_file_exists() function this path is followed
                print(f'Error: Filename {PNG_filenames} already exists in folder.\n') # printing the error that the histogram already exists

# fetching data from csv file
df = pd.read_csv('iris_data.csv')

# Filtering the dataset based on class to be able to differeniate in plots later in the program
setosa_df = df[df['class'] == 'Iris-setosa']
versicolor_df = df[df['class'] == 'Iris-versicolor']
virginica_df = df[df['class'] == 'Iris-virginica']

# Setting variables for comparison across the classes  which will be used for the subplots on the scatter plot
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
intro = (f'The IRIS dataset, created in 1936, is a popular dataset commonly used for exploring data analysis and data visualisation.\n\nSpecies:\n\tThe dataset consists of measurements for 3 different classes (Setosa, Versicolor and Virginica) of Iris flowers.\nThere are 50 entries per class detailed in the dataset.\nAs the classes variable are plain text, the data type string will be applicable here.\n\nFour characteristics of the flowers were tracked including sepal length (cm), sepal width (cm), petal length (cm) and petal width (cm)\nThese four variables are numeric values and looking at the raw data we can see decimal places are present.\nWith this, the data type used for this variables will be float.\n\n')

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

#####################################################################################
#    Idea for new plot > decide if there is anything insightful from the visual     #
#####################################################################################

def setting_axis_limits(ymin, ymax): # function to overwrite the range automatically populated for plots and instead use set values for ranges for the x and y axis 
    plt.ylim(ymin, ymax) # setting min and max values for the y axis 
    #plt.xlim(xmin, xmax) # setting the min and max values for the y axis

def set_bins_width(histogram_to_plot):
        # Compute the bin edges based on the overall range of petal widths
        min_width = min(setosa_df[histogram_to_plot].min(), versicolor_df[histogram_to_plot].min(), virginica_df[histogram_to_plot].min())
        max_width = max(setosa_df[histogram_to_plot].max(), versicolor_df[histogram_to_plot].max(), virginica_df[histogram_to_plot].max())
        bin_edges = np.linspace(min_width, max_width, 11)  # 10 bins with equal width
        return bin_edges

histogram_to_plot = 'sepal length (cm)'
# Compute the bin edges
bin_edges = set_bins_width(histogram_to_plot)
# Additional plot of histograms looking at individual species alone

# Setting variables for comparison across the species which will be used for the subplots
# sepal length vs sepal width, sepal length vs petal length, sepal length vs petal width
# sepal width vs petal length, sepal width vs petal width
# petal length vs petal width
# petal width
plt.figure(figsize=(9, 12))
plt.subplots_adjust(top=1)

ymin = 0
ymax = 19.5
set_bins_width(histogram_to_plot)
plt.subplot(4, 3, 1)  # Creating a subplot for sepal length vs sepal width
setting_axis_limits(ymin, ymax)
plt.hist(setosa_sepal_length, bins=bin_edges, color='violet')
plt.yticks([])
plt.title('--------------------', fontsize = 20)

plt.subplot(4, 3, 2)  # Creating a subplot for sepal length vs petal length
setting_axis_limits(ymin, ymax)
plt.hist(versicolor_sepal_length, bins=bin_edges, color='navy')
plt.yticks([])
plt.title('Sepal Length (cm)', fontsize = 20)

plt.subplot(4, 3, 3)  # Creating a subplot for sepal length vs petal width
setting_axis_limits(ymin, ymax)
plt.hist(virginica_sepal_length, bins=bin_edges, color='orange')
plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False, labelleft=False)
plt.title('--------------------', fontsize = 20)

ymax = 16.5
histogram_to_plot = 'sepal width (cm)'
# Compute the bin edges
bin_edges = set_bins_width(histogram_to_plot)
plt.subplot(4, 3, 4) # Creating plot for sepal width vs petal length
setting_axis_limits(ymin, ymax)
plt.hist(setosa_sepal_width, bins=bin_edges, color='violet', label='Setosa')
plt.title('--------------------', fontsize = 20)
plt.yticks([])

plt.subplot(4, 3, 5) # Creating plot for sepal width vs petal width
setting_axis_limits(ymin, ymax)
plt.hist(versicolor_sepal_width, bins=bin_edges, color='navy', label='Versicolor')
plt.yticks([])
plt.title('Sepal Width (cm)', fontsize = 20)

plt.subplot(4, 3, 6) # Creating plot for petal length vs petal width
setting_axis_limits(ymin, ymax)
plt.hist(virginica_sepal_width, bins=bin_edges, color='orange', label='Virginica')
plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False, labelleft=False)
plt.title('--------------------', fontsize = 20)

ymax = 38
histogram_to_plot = 'petal length (cm)'
# Compute the bin edges
bin_edges = set_bins_width(histogram_to_plot)
# Compute the bin edges based on the overall range of petal widths

plt.subplot(4, 3, 7) 
setting_axis_limits(ymin, ymax)
plt.hist(setosa_petal_length, bins=bin_edges, color='violet')
plt.yticks([])
plt.title('--------------------', fontsize = 20)

plt.subplot(4, 3, 8)
setting_axis_limits(ymin, ymax)
plt.hist(versicolor_petal_length, bins=bin_edges, color='navy')
plt.yticks([])
plt.title('Petal Length (cm)', fontsize = 20)

plt.subplot(4, 3, 9)
setting_axis_limits(ymin, ymax)
plt.hist(virginica_petal_length, bins=bin_edges, color='orange')
plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False, labelleft=False)
plt.title('--------------------', fontsize = 20)

ymax = 42
histogram_to_plot = 'petal width (cm)'
bin_edges = set_bins_width(histogram_to_plot)
plt.subplot(4, 3, 10)
setting_axis_limits(ymin, ymax)
plt.hist(setosa_petal_width, bins=bin_edges, color='violet')
plt.title('--------------------', fontsize = 20)
plt.yticks([])

plt.subplot(4, 3, 11)
setting_axis_limits(ymin, ymax)
plt.hist(versicolor_petal_width, bins=bin_edges, color='navy')
plt.yticks([])
plt.title('Petal Width (cm)', fontsize = 20)

plt.subplot(4, 3, 12)
setting_axis_limits(ymin, ymax)
plt.hist(virginica_petal_width, bins=bin_edges, color='orange',)
# Adjusting ticks on y-axis
plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False, labelleft=False)
plt.title('--------------------', fontsize = 20)

plt.tight_layout()
plt.suptitle('Histograms per class', y=1.08, fontsize=32)
plt.figlegend(loc = "upper center", ncols = 3, bbox_to_anchor=(0.5, 1.04), fontsize=14) # creating one legend for the subplots and setting it's location to the top center for the plot
plt.savefig("6_classes_histogram.png", bbox_inches='tight') # saving scatter plot as PNG file with bbox_inches set to tight to adjust the title
