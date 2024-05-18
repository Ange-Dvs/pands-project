# analysis.py
# This program reads in the IRIS dataset and performs analysis and generation of plots using the data. 
# The generated plots are saved as .png files and a summary .txt file is created.
# Author: Angela Davis

#importing the libraries to use in the program
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from tabulate import tabulate as tb

#Creating functions that will be used in the program

def check_png_file_exists(PNG_filenames): # creating a function which will check if the PNG files are already existing before trying to create them
    if os.path.exists(PNG_filenames): # using OS library the value set in "PNG_filenames" (defined outside of the function) is used to check if the file is already existing 
        raise FileExistsError # if the file exists the FileExists Error is thrown and it triggers the except path outside the function

def write_summary_file(xy_value, dfs_to_use): # creating a function which will create the text file called IRIS_Summary.txt when one does not already exist. If it exists error is printed for user
        text_file_name = 'IRIS_Summary.txt' # setting file name
        try: # first the new text file is attempted to be created 
                with open(text_file_name, 'x', encoding='utf-8') as f: # "x" creates a new text file and the text_file_name variable defined at the beginning of the main code block is used to name the file. UTF-8 encoding is used to allow the table generated using tabulate to be added to the text file 
                        num_values = df.describe() # getting a summary of the numerical values for  the entire dataset using .describe()
                        # filtering the data by the class and getting a summary of the numerical variables
                        setosa_info = df[df['class'] == 'Iris-setosa'].describe()
                        versicolor_info = df[df['class'] == 'Iris-versicolor'].describe()
                        virginica_info = df[df['class'] == 'Iris-virginica'].describe()
                        length_df = len(df) # checking the number of entries in the dataset
                        data_types = df.dtypes # checking the data types of the variables in the dataset
                        count_class = df['class'].value_counts() # getting the count of the entries in the dataset per class of Iris
                        # setting the main text for the summary file using the variables defined above
                        intro = (f'\t\t\t\t\t\t**** The IRIS dataset ****\n\nCreated in 1936, the Iris dataset is a popular dataset commonly used for exploring data analysis and data visualisation.\n\nThe dataset consists of measurements for 3 different classes (Setosa, Versicolor and Virginica) of Iris flowers. The number of rows in the dataset is {length_df}, meaning the we have the information for 150 Iris flowers tracked. To see how many entries are tracked per class of Iris we can use the value_count method.\n\n\t{count_class}.\n\nFrom the above we can see there are 50 entries per class detailed in the dataset, so each class accounts for a third of the entries in the dataset. As the class variable is plain text, the data type string will be applicable here.\n\nFour characteristics of the flowers were tracked including sepal length, sepal width, petal length and petal width. These four variables are numeric values and looking at the raw data we can see decimal places are present. With this, the data type used for this variables will be float. We can check this easily using pandas in python.\n\nVariable:\t\tData type:\n{data_types}\n\nFrom the above we can see that the data type for the numerical variables is in fact a float. For the class variable we can see object is stated. Within pandas the object data type is the most general data type and can hold any Python objects including strings.\n\nNext we will generate some statistical information which will be analysed in the README.ipynb in further details.\n\nNumerical summary looking only of all classes together:\n{num_values}\n\nNumerical summary looking only at the Setosa class:\n{setosa_info}\n\nNumerical summary looking only at the Versicolor class:\n{versicolor_info}\n\nNumerical summary looking only at the Virginica class:\n{virginica_info}\n')
                        f.write(intro) # writing intro into the text file, since the intro is a string already it doesn't need to be cast as string before writing

                        correlations = {} # creating an empty dictionary to be used to store the calculated values for the correlation coefficient in the for loop below
                        for (classes) in (dfs_to_use): # looping through the dfs_to_use 
                                for i, (x_value, y_value) in enumerate(xy_value, start=1): # looping through the xy_values list and setting the values in the tuples to x_values & y_values
                                        if i in [2, 3, 4, 7, 8, 12]: # next setting a condition for which iterations to perform the calculation, if i (iteration counter) is one of the values in the list it follows this step
                                                corr_calculated = float(dfs_to_use[classes][x_value].corr(dfs_to_use[classes][y_value])) # correlation coefficient is calculated and answer set to a float to ensure decimal place numbers can be handled
                                                name = (f'{classes} {x_value} vs {y_value}') # creates a value to be set as "name" using the species specified in the first for loop
                                                correlations[name] = corr_calculated # then this name is added to the correlations dictionary with the corresponding calculated coefficient as a keypair
                        corr_table = [ # creating a table which will show the calculated correlation coefficient overall for the entire DF then breaking it down per class of Iris too see how the class of Iris effects the correlation coefficient for a pair of variables.
                        ['Correlation\ncoefficient','Sepal Width\nvs.    \nSepal Length','Petal Length\nvs.    \nSepal Length','Petal Width\nvs.    \nSepal Length','Petal Length\nvs.    \nSepal Width','Petal Width\nvs.    \nSepal Width','Petal Width\nvs.    \nPetal Length'],
                        ['All classes', correlations['All classes - sepal width vs sepal length'], correlations['All classes - petal length vs sepal length'], correlations['All classes - petal width vs sepal length'], correlations['All classes - petal length vs sepal width'], correlations['All classes - petal width vs sepal width'], correlations['All classes - petal width vs petal length']],
                        ['Setosa', correlations['Setosa - sepal width vs sepal length'], correlations['Setosa - petal length vs sepal length'], correlations['Setosa - petal width vs sepal length'], correlations['Setosa - petal length vs sepal width'], correlations['Setosa - petal width vs sepal width'], correlations['Setosa - petal width vs petal length']],
                        ['Versicolor', correlations['Versicolor - sepal width vs sepal length'], correlations['Versicolor - petal length vs sepal length'], correlations['Versicolor - petal width vs sepal length'], correlations['Versicolor - petal length vs sepal width'], correlations['Versicolor - petal width vs sepal width'], correlations['Versicolor - petal width vs petal length']],
                        ['Virginica', correlations['Virginica - sepal width vs sepal length'], correlations['Virginica - petal length vs sepal length'], correlations['Virginica - petal width vs sepal length'], correlations['Virginica - petal length vs sepal width'], correlations['Virginica - petal width vs sepal width'], correlations['Virginica - petal width vs petal length']]                       
                        ]

                        table_to_print = tb(corr_table, headers='firstrow', tablefmt='fancy_grid') # casting the list to a table layout using tabulate and setting the table to have headers in the first row and using the fancy grid format to make the table look neater 
                        
                        f.write(f'\nCorrelation per pair of variables:\n') # writing a line to the text file to explain what the table is
                        f.write(table_to_print) # adding the table to the text file

        except FileExistsError: # if the file exists when it is attempted to use "x" to create the file then a FileExistsError is thrown
                print (f'\nError: Filename {text_file_name} already exists in folder.\n') # This message will be printed to the user if the FileExistsError is triggered

def create_histograms(variables_and_filenames): # creating a function which can be reused to create a histogram of each variable and also to check if the file is already existing
        for variable_to_plot, PNG_filenames in variables_and_filenames.items(): # Iterate over variables and filenames in variables and filename dictionary
                try: # First this path is attempted to be executed
                        check_png_file_exists(PNG_filenames) # the function earlier created to check if the .png file already exists is triggered. If the file does not exist the code will continue to the next line. If the file does already exist the FileExistsError will be thrown and the code will jump to the except condition
                        plt.figure(figsize=(10,5)) # figure size is set to avoid the plot being overloaded and make it more readable for the user
                        plt.subplot(1, 2, 1) # number of rows and columns needed for the subplot is defined
                        plt.hist(df[variable_to_plot]) # histogram is created using the value assigned to the variable_to_plot variables and the check the entire dataset
                        plt.title('All classes of Iris together') # adding the title to the first subplot

                        plt.subplot(1, 2, 2) # plotting the subplot to be placed in the second column
                        all_sepal_lengths = [df[df['class'] == 'Iris-setosa'][variable_to_plot], df[df['class'] == 'Iris-versicolor'][variable_to_plot], df[df['class'] == 'Iris-virginica'][variable_to_plot]] # using the filtered datasets to select the information per class of Iris to enable colour coding of the histogram per class

                        plt.hist(all_sepal_lengths, # plotting the histogram showing the breakdown per class of Iris colour coded
                                stacked=True, # stacked enables stacking the data into neat columns with the species showing in a towered way on top of each other 
                                label=['Setosa', 'Versicolor', 'Virginica'], # assigning the labels for the legend
                                edgecolor='white', # setting the colour of the outline of the bins
                                color=['violet', 'navy', 'orange']) # setting the colour of the columns
                        plt.title('Colour coded per class of Iris') # adding the title to the second subplot
                        plt.yticks([]) # removing y ticks since the same y values are used as shown in the subplot in the first position to tidy up plot

                        plt.tight_layout() # avoiding any overlap in text or plots in the figure 
                        plt.legend() # generating the legend using the labels set above

                        plt.suptitle(f'Distribution of {variable_to_plot}', fontsize = 18, y= 1.05) # setting the overall title for the figure
                        # Adding a super x label to replace having two separate labels for the x axis setting the  position of the text, alignment, fontsize and style
                        plt.figtext(0.5, -0.01, f'{variable_to_plot} (cm)', ha='center', fontsize=14, fontstyle='italic')

                        plt.savefig(PNG_filenames, bbox_inches='tight') # saving histograms as a PNG file with bbox_inches set to tight to avoid any text or info being cut from the figure

                        print(f'{PNG_filenames} created.\n') # printing the confirmation for a histograms creation specifying the filename of the file created using the PNG_filename variable

                except FileExistsError: # If the PNG file is found to already exist when calling check_png_file_exists() function this path is triggered as the next step
                        print(f'Error: Filename {PNG_filenames} already exists in folder. \n') # printing the error that the histogram already exists

def create_scatter_all_variables(xy_value, dfs_to_use): # creating a function which is generating the scatter plot with showing all variables compared to each other
        PNG_filenames = 'scatter_all_variables.png'
        plt.figure(figsize=(9, 9)) # figure size is set to avoid the plot being overloaded
        # Iterate over variables and filenames
        try: 
                check_png_file_exists(PNG_filenames) # the function earlier created to check if the png file exists is triggered. If the file does not exist the code will continue to the next line. If the file does already exist the FileExistsError will be thrown and the code will jump to the except condition.
                for i, (x_value, y_value) in enumerate(xy_value, start=1):
                        if i in (1, 6, 11, 16): # if the value for i matches any defined in the condition this path will be triggered by the program
                                plt.subplot(4,4,i) # creating the subplots for the two variables passed each loop using value assigned for i to set the position of the subplot
                                # removing x & y ticks
                                plt.yticks([])
                                plt.xticks([])
                                plt.plot()
                                if i == 1:
                                        plt.figtext(.14, .82, 'Sepal\nLength', ha='center', fontsize=22, fontstyle='italic')
                                elif i == 6:
                                        plt.figtext(.385, .585, 'Sepal\nWidth', ha='center', fontsize=22, fontstyle='italic')
                                elif i == 11:
                                        plt.figtext(.625, .355, 'Petal\nLength', ha='center', fontsize=22, fontstyle='italic')
                                elif i == 16:
                                        plt.figtext(.86, .12, 'Petal\nWidth', ha='center', fontsize=22, fontstyle='italic')
                                        plt.tight_layout()
                                        plt.suptitle('All variables', y=1.08, fontsize=32) # adding an overall title for the figure with a specified font size and position
                                        plt.figlegend(loc = 'upper center', ncols = 3, bbox_to_anchor=(0.5, 1.04), fontsize=14, labels=['Setosa', 'Versicolor', 'Virginica']) # creating one legend for the subplots and setting it's location to the top centre for the plot. Manually setting the labels to avoid it being set repeatedly in the loop
                                        plt.savefig(PNG_filenames, bbox_inches='tight') # saving scatter plot as PNG file with bbox_inches set to tight to adjust to fit the whole figure
                                        print(f'{PNG_filenames} created.\n') # printing the confirmation for a histograms creation
                        else:
                                plt.subplot(4,4,i) # creating the subplots for the two variables passed each loop using value assigned for i to set the position of the subplot
                                for class_name, class_df in dfs_to_use.items(): # assigning the colour to use for the markers depending on the class name used for the loop also creating the scatter plot provided the class name is not 'All classes -'
                                        if class_name == 'Setosa -':
                                                marker_colour = 'violet'
                                        elif class_name == 'Versicolor -':
                                                marker_colour = 'navy'
                                        elif class_name == 'Virginica -':
                                                marker_colour = 'orange'
                                        else: # to catch any other values
                                                marker_colour = 'black'
                                        
                                        if class_name != 'All classes -': # ensuring only the filtered numbers for the datasets per class are used in the scatter plot
                                                plt.scatter(class_df[x_value], class_df[y_value], color= marker_colour) # creating the scatter plot
                                        
                                        # next the program will pass through one of the following conditions for further customization if the value for i is matching one defined for the path
                                        if i in (3, 7, 8, 9, 10, 14): # removing of x and y ticks 
                                                plt.yticks([])
                                                plt.xticks([])
                                        elif i == 2: # removing of y ticks and moving the x ticks to the top of the plot for easier readability and to reflect every plot in that column
                                                plt.yticks([])
                                                plt.tick_params(axis='x', direction='out', top=True, labeltop=True, bottom=False, labelbottom=False)
                                        elif i == 4: # moving the x & y ticks to the top of the plot for easier readability and to reflect every plot in that column
                                                plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False, labelleft=False)
                                                plt.tick_params(axis='x', direction='out', top=True, labeltop=True, bottom=False, labelbottom=False)
                                        elif i == 5: # removing x ticks
                                                plt.xticks([])
                                        elif i == 12: # removing of x ticks and moving the y ticks to the right of the plot for easier readability and to reflect every plot in that row
                                                plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False, labelleft=False)
                                                plt.xticks([])
                                        elif i == 15: # removing y ticks
                                                plt.yticks([])
        
        except FileExistsError: # If the PNG file is found to already exist when calling check_png_file_exists() function this path is followed
                print(f'Error: Filename {PNG_filenames} already exists in folder.\n') # printing the error that the histogram already exists

def setting_axis_limits(s): # creating a function which will set the range for the y axis
    ymin = 0 # 0 always the min
    if s in (1, 2, 3): # following if s equals value in list
        ymax = 19.5
    elif s in (4, 5, 6):
        ymax = 16.5
    elif s in (7, 8, 9):
        ymax = 38
    elif s in (10, 11, 12):
        ymax = 42
    plt.ylim(ymin, ymax)# setting the range for the y axis in the plot

def set_bins_width(variable_to_plot, df):
        # Setting the bin edges based on the overall range of the variables
        min_width = df[variable_to_plot].min() # finding the min value for the variable passed in the loop in the dataset
        max_width = df[variable_to_plot].max() # finding the max value for the variable passed in the loop in the dataset 
        bin_edges = np.linspace(min_width, max_width, 11) # creating an array of 11 evenly spaced numbers within the range of the min and max values set to the min_width and max_width variable. This will ensure that each of the histogram has space for 10 evenly spaced bins within that entire range
        return bin_edges # returning the value of the bins

def create_histogram_per_classes(variables_and_filenames, dfs_to_use, df):
        PNG_filenames = 'hist_all_variables_per_species.png' # setting PNG filename to use
        try: # first this block of code will be attempted if FileExistsError is thrown program skips to the except code block
                check_png_file_exists(PNG_filenames) # checking if the file exists
                plt.figure(figsize=(9, 14)) # setting the figure size to ensure it is big enough to comfortably fit the subplots of the histograms
                s = 1 # setting s initially as 1 to be used for the subplot number in the loops
                for variable_to_plot in variables_and_filenames: # looping the code for each of the variables that need to be plotted in the variables and filenames dictionary
                        bin_edges = set_bins_width(variable_to_plot, df) # calling the function to set the width of the bins
                        for i, (class_name, class_df) in enumerate(dfs_to_use.items(), start=1): # unpacking the dfs_to_use dictionary to set the class_df dynamically depending on the iteration of the loop
                                if i != 1: # checking to ensure that i is not equals to 1 as we are not interested in the histogram of the entire dataset for this figure, only the individual classes
                                        plt.subplot(4, 3, s) # dynamically setting the subplot position using the value assigned to s
                                        if s in (1, 4, 7, 10): # program will execute this block of code if the value for s matches one of the values in brackets
                                                colour_to_use = 'violet'
                                                plt.yticks([])
                                        elif s in (2, 5, 8, 11): # program will execute this block of code if the value for s matches one of the values in brackets
                                                colour_to_use = 'navy' # setting colour for bins
                                                plt.yticks([]) # removing y ticks since it will be the same range as the last plot in each row
                                                plt.xlabel(f'{variable_to_plot} in (cm)', fontsize=20) # adding a label which will dynamically set the x label to the middle plot in each row 
                                        else: # this should mean 3, 6, 9, 12 pass through this block
                                                colour_to_use = 'orange' # setting the colour for the bins
                                                plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False,
                                                                labelleft=False) # moving the y ticks and labels to the right side of the plot
                                        plt.title('--------------------------', fontsize=20) # adding dashes as the title to help separate the subplots based on the variables
                                        setting_axis_limits(s) # calling function for setting the limits for the range on the y axis
                                        plt.hist(class_df[variable_to_plot], bins=bin_edges, color=colour_to_use) # plotting the histogram setting the number of bins and colour of the bins
                                        if s == 12: # checking is s equals 12 as this is the last subplot so figure should be saved and some details added
                                                plt.tight_layout()
                                                plt.suptitle('Histograms per class', y=1.075, fontsize=32) # adding an overall title for the figure with a specified font size and position
                                                plt.figlegend(loc='upper center', ncols=3, bbox_to_anchor=(0.5, 1.035), fontsize=14,
                                                        labels=['Setosa', 'Versicolor', 'Virginica']) # creating one legend for the subplots and setting it's location to the top center for the plot. Manually setting the labels to avoid it being set repeatedly in the loop
                                                plt.savefig(PNG_filenames, bbox_inches='tight') # saving figure with bbox_inches set to tight to adjust to fit the whole figure 
                                                print(f'{PNG_filenames} created.\n') # printing confirmation message to user
                                        s += 1 # value of s is increased by 1 to allow for the next subplot to be created 

        except FileExistsError: # following this path if file exists
                print(f'\nError: Filename {PNG_filenames} already exists in folder.\n') # printing error for user

def hist_all_df_all_variables(variables_and_filenames):
        PNG_filenames= 'hist_variables_overview.png'
        try:
                check_png_file_exists(PNG_filenames)
                plt.figure(figsize=(10,10)) # figure size is set to avoid the plot being overloaded and make it more readable for the user
                for i, variable_to_plot in enumerate(variables_and_filenames, start=1): # Iterate over variables and filenames in variables and filename dictionary
                        plt.subplot(2, 2, i) # number of rows and columns needed for the subplot is defined
                        plt.hist(df[variable_to_plot]) # histogram is created using the value assigned to the variable_to_plot variables and the check the entire dataset
                        plt.xlabel(f'{variable_to_plot} (cm)', fontsize=14)

                        if i == 4: 
                                plt.suptitle('All classes of Iris together', y=.98, fontsize=18) # adding the title to the first subplot
                                plt.tight_layout()
                                plt.savefig(PNG_filenames, bbox_inches='tight') # saving histograms as a PNG file with bbox_inches set to tight to avoid any text or info being cut from the figure
                                print(f'{PNG_filenames} created.\n') # printing the confirmation for a histograms creation
                                
        except FileExistsError: # If the PNG file is found to already exist when calling check_png_file_exists() function this path is followed
                print(f'Error: Filename {PNG_filenames} already exists in folder.\n') # printing the error that the histogram already exists

original_df = pd.read_csv('iris_data.csv')      # fetching data from csv file

# Tidying up the dataset so that it is the items printed to the summary file are more readable, i.e. the output of df.describe() would be split due to the length of the column headers by checking for the original df for " (cm)" and deleting it
original_df.columns = original_df.columns.str.replace(' (cm)', '')

# Check if the file already exists
if os.path.exists('modified_iris_data.csv'):
        print('\nError: Filename modified_iris_data.csv already exists in folder.')
else:
        # Saving modified dataset back to a new CSV file so that we can use the tidied information for the plots
        original_df.to_csv('modified_iris_data.csv', index=False)
        print('\nmodified_iris_data.csv created\n')

df = pd.read_csv('modified_iris_data.csv') # fetching data from the new tidied csv file

# Defining list of variables to plot for x axis value and y axis value for scatter plot png
xy_value = [('',''), ('sepal width', 'sepal length'), ('petal length', 'sepal length'), ('petal width', 'sepal length'), ('sepal length', 'sepal width'), ('',''), ('petal length', 'sepal width'), ('petal width', 'sepal width'), ('sepal length','petal length'), ('sepal width', 'petal length'), ('',''), ('petal width', 'petal length'), ('sepal length', 'petal width'), ('sepal width', 'petal width'), ('petal length','petal width'), ('','')]

dfs_to_use = {'All classes -': df,'Setosa -': df[df['class'] == 'Iris-setosa'], 'Versicolor -': df[df['class'] == 'Iris-versicolor'], 'Virginica -': df[df['class'] == 'Iris-virginica']} # setting keypairs to be used for the loop when calculating the correlation coefficient. The df will then be possible to call using the value set as the name. It also filters the dataset based on class to be able to differeniate in plots later in the program

# Defining dictionary of variables to plot for histograms and filenames for the individual histogram .pngs
variables_and_filenames = {
    'sepal length': 'hist_sepal_length.png',
    'sepal width': 'hist_sepal_width.png',
    'petal length': 'hist_petal_length.png',
    'petal width': 'hist_petal_width.png'}

write_summary_file(xy_value, dfs_to_use) # calling function to create summary text file

create_histograms(variables_and_filenames) # calling function to create the required histograms per variable in the dataset

create_scatter_all_variables(xy_value, dfs_to_use) # calling function to create the scatter plot comparing all variables 

create_histogram_per_classes(variables_and_filenames, dfs_to_use, df) # calling function which is creating a figure with all variables plotted to histograms filtered by class of Iris

hist_all_df_all_variables(variables_and_filenames) # figure showing the high level plots of all variables in the dataset