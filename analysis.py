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

                print(f'{PNG_filenames} created.\n') # printing the confirmation for a histograms creation 

        except FileExistsError: # If the PNG file is found to already exist when calling check_png_file_exists() function this path is followed
                print(f'Error: Filename {PNG_filenames} already exists in folder. \n') # printing the error that the histogram already exists

def create_scatter_all_variables(x_variable, y_variable, PNG_filenames):
        if i == 1 or i == 6 or i == 11 or i == 16:
                plt.subplot(4,4,i)
                plt.yticks([])
                plt.xticks([])
                plt.plot()
                if i == 1:
                        plt.figtext(.16, .82, 'Sepal\nLength', ha='center', fontsize=22, fontstyle='italic')
                elif i == 6:
                        plt.figtext(.39, .59, 'Sepal\nWidth', ha='center', fontsize=22, fontstyle='italic')
                elif i == 11:
                        plt.figtext(.63, .35, 'Petal\nLength', ha='center', fontsize=22, fontstyle='italic')
                elif i == 16:
                        plt.figtext(.86, .12, 'Petal\nWidth', ha='center', fontsize=22, fontstyle='italic')
                        plt.tight_layout()
                        plt.suptitle('All variables', y=1.08, fontsize=32)
                        plt.figlegend(loc = "upper center", ncols = 3, bbox_to_anchor=(0.5, 1.04), fontsize=14, labels=['Setosa', 'Versicolor', 'Virginica']) # creating one legend for the subplots and setting it's location to the top center for the plot. Manually setting the labels to avoid it being set repeatly in the loop
                        plt.savefig(PNG_filenames, bbox_inches='tight') # saving scatter plot as PNG file with bbox_inches set to tight to adjust to fit the whole figure
                        print(f'{PNG_filenames} created.\n') # printing the confirmation for a histograms creation
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
                        plt.xticks([])
                elif i == 15:
                        plt.yticks([])

def setting_axis_limits(): # function to overwrite the range automatically populated for plots and instead use set values for ranges for y axis 
    ymin = 0
    if i == 1:
        ymax = 19.5
    elif i == 2:
        ymax = 16.5
    elif i == 3:
        ymax = 38
    else: 
        ymax = 42
    plt.ylim(ymin, ymax) # setting min and max values for the y axis 

def set_bins_width(variable_to_plot):
        # Compute the bin edges based on the overall range of the variables
        min_width = min(setosa_df[variable_to_plot].min(), versicolor_df[variable_to_plot].min(), virginica_df[variable_to_plot].min())
        max_width = max(setosa_df[variable_to_plot].max(), versicolor_df[variable_to_plot].max(), virginica_df[variable_to_plot].max())
        bin_edges = np.linspace(min_width, max_width, 11)  # 10 bins with equal width
        return bin_edges

def create_histogram_per_classes(s, variable_to_plot, PNG_filenames):
        bin_edges = set_bins_width(variable_to_plot)
        plt.subplot(4, 3, s)  # Creating a subplot for sepal length vs sepal width
        setting_axis_limits()
        plt.hist(setosa_df[variable_to_plot], bins=bin_edges, color='violet')
        plt.yticks([])
        plt.title('--------------------', fontsize = 20)

        plt.subplot(4, 3, s+1)  # Creating a subplot for sepal length vs sepal width
        setting_axis_limits()
        plt.hist(versicolor_df[variable_to_plot], bins=bin_edges, color='navy')
        plt.yticks([])
        plt.title(variable_to_plot, fontsize = 20)
        
        plt.subplot(4, 3, s+2)  # Creating a subplot for sepal length vs petal width  
        setting_axis_limits()
        plt.hist(virginica_df[variable_to_plot], bins=bin_edges, color='orange')
        plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False, labelleft=False)
        plt.title('--------------------', fontsize = 20)
        if s+2 == 12:
                plt.tight_layout()
                plt.suptitle('Histograms per class', y=1.08, fontsize=32)
                plt.figlegend(loc = "upper center", ncols = 3, bbox_to_anchor=(0.5, 1.04), fontsize=14, labels=['Setosa', 'Versicolor', 'Virginica']) # creating one legend for the subplots and setting it's location to the top center for the plot
                plt.savefig(PNG_filenames, bbox_inches='tight') # saving scatter plot as PNG file with bbox_inches set to tight to adjust the title
                print(f'{PNG_filenames} created.\n') # printing the confirmation for a histograms creation

# fetching data from csv file
df = pd.read_csv('iris_data.csv')

# Filtering the dataset based on class to be able to differeniate in plots later in the program
setosa_df = df[df['class'] == 'Iris-setosa']
versicolor_df = df[df['class'] == 'Iris-versicolor']
virginica_df = df[df['class'] == 'Iris-virginica']

# Printing a summary of the numeric valyes of the dataset
num_values = df.describe()
intro = (f'The IRIS dataset, created in 1936, is a popular dataset commonly used for exploring data analysis and data visualisation.\n\nSpecies:\n\tThe dataset consists of measurements for 3 different classes (Setosa, Versicolor and Virginica) of Iris flowers.\nThere are 50 entries per class detailed in the dataset.\nAs the classes variable are plain text, the data type string will be applicable here.\n\nFour characteristics of the flowers were tracked including sepal length (cm), sepal width (cm), petal length (cm) and petal width (cm)\nThese four variables are numeric values and looking at the raw data we can see decimal places are present.\nWith this, the data type used for this variables will be float.\n\n')

# Define dictionary of variables to plot for histograms and filenames for the individual histogram pngs
variables_and_filenames = {
    'sepal length (cm)': '1_sepal_length_hist.png',
    'sepal width (cm)': '2_sepal_width_hist.png',
    'petal length (cm)': '3_petal_length_hist.png',
    'petal width (cm)': '4_petal_width_hist.png'}

write_summary_file(FILENAME)
 
# Iterate over variables and filenames
for i, (variable_to_plot, PNG_filenames) in enumerate(variables_and_filenames.items()):
       create_histograms(PNG_filenames, variable_to_plot)

# Define lsit of variables to plot for x axis value and y axis value for scatter plot png
x_variables_y_variables = [('',''), ('sepal width (cm)', 'sepal length (cm)'), ('petal length (cm)', 'sepal length (cm)'), ('petal width (cm)', 'sepal length (cm)'), ('sepal length (cm)', 'sepal width (cm)'), ('',''), ('petal length (cm)', 'sepal width (cm)'), ('petal width (cm)', 'sepal width (cm)'), ('sepal length (cm)','petal length (cm)'), ('sepal width (cm)', 'petal length (cm)'), ('',''), ('petal width (cm)', 'petal length (cm)'), ('sepal length (cm)', 'petal width (cm)'), ('sepal width (cm)', 'petal width (cm)'), ('petal length (cm)','petal width (cm)'), ('','')]

PNG_filenames = '5_all_variables_scatter.png'
# Iterate over variables and filenames
plt.figure(figsize=(9, 9)) # figure size is set to avoid the plot being overloaded
for i, (x_variable, y_variable) in enumerate(x_variables_y_variables, start=1):
        try: 
                check_png_file_exists(PNG_filenames) # the function earlier created to check if the png file exists is triggered. If the file does not exist the code will continue to the next line. If the file does already exist the FileExistsError will be thrown and the code will jump to the except condition.   
                create_scatter_all_variables(x_variable, y_variable, PNG_filenames)   

        except FileExistsError: # If the PNG file is found to already exist when calling check_png_file_exists() function this path is followed
                print(f'Error: Filename {PNG_filenames} already exists in folder.\n') # printing the error that the histogram already exists
                break

s=1
PNG_filenames = '6_classes_histogram.png'
plt.figure(figsize=(9, 12)) # figure size is set to avoid the plot being overloaded
for i, (variable_to_plot) in enumerate(variables_and_filenames, start=1):
        try:
                check_png_file_exists(PNG_filenames) # the function earlier created to check if the png file exists is triggered. If the file does not exist the code will continue to the next line. If the file does already exist the FileExistsError will be thrown and the code will jump to the except condition.
                create_histogram_per_classes(s, variable_to_plot, PNG_filenames)
                s += 3
                
        except FileExistsError: # If the PNG file is found to already exist when calling check_png_file_exists() function this path is followed
                print(f'Error: Filename {PNG_filenames} already exists in folder.\n') # printing the error that the histogram already exists
                break