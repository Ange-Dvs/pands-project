# <font color='purple'>IRIS dataset </font>
***

## Summary of IRIS dataset:
***

The IRIS dataset, created in 1936, is a popular dataset commonly used for exploring data analysis and data visualisation.

The dataset consists of measurements for 3 different species (setosa, versicolor and virginica) of Iris flowers.  
There are 50 entries per species detailed in the dataset.

### Species:
|Setosa    |Versicolor | Virginica|
|-----------|---------------|------------|
|![Setosa](https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/180px-Kosaciec_szczecinkowaty_Iris_setosa.jpg)|![Versicolor](https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Iris_versicolor_3.jpg/320px-Iris_versicolor_3.jpg)|![Virginica](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/295px-Iris_virginica.jpg)|

As the species variable are plain text, the data type string will be applicable here.

Four characteristics of the flowers were tracked including sepal length, sepal width, petal length and petal width.  
These four variables are numeric values and looking at the raw data we can see decimal places are present. 
With this, the data type used for this variables will be float.

## Cloning repository from GitHub:
***

1. Copy the following URL:  
        https://github.com/Ange-Dvs/pands-project.git

1. Open CMDER or if using VS Code open the terminal pane

1. Go to the folder where you want to clone the repository to on your machine and type git pull.  
        ![git clone link](Images_for_readme/image-3.png)

1. Set merge as the mode for the pull  
        ![git rebase](Images_for_readme/image-4.png)

1. Initiate the pull of the GitHub repository  
        ![git pull](Images_for_readme/image-5.png)

1. If the pull has been successful you should see 4 files pulled from GitHub
        The .gitignore file, a csv file containing the dataset, the readme in the form of a Jupyter notebook and the analysis.py file which contains the program to run.  
        !!!!!! INSERT SCREENSHOT OF CLEAN REPO

## How to run *analysis.py*:
***

1. To run the code open CMDER or the terminal in VS Code.
1. Navigate to the folder where the repository is stored.
1. Type ![triggering analysis.py to run](Images_for_readme/image-6.png) and hit enter. 
1. The python code should run and generate 8 files.
    - modified_iris_data.csv created
    - hist_sepal_length.png created.
    - hist_sepal_width.png created.
    - hist_petal_length.png created.
    - hist_petal_width.png created. 
    - scatter_all_variables.png created. 
    - hist_all_variables_per_species.png created. 
1. If the code has run successfully you will see confirmation printed when each file is created.  
        ![file confirmation messages](Images_for_readme/image-7.png)

### Error handling within *analysis.py*:

Error handling is including in the code to ensure if a file is already existing in the folder with the same filename the user will be informed.

The error messages will look like this:  

![error messages](Images_for_readme/image-8.png)

If the error message for a file is returned that file will not be re-created or overwritten.
If you want to rerun the code and create the files again, you'll need to delete the existing file or files first.    

## Walkthrough of *analysis.py* code:
***
The next section of the notebook is a walkthrough of the contents of the analysis.py file.  
While the functionality will be explained in this notebook, a line by line explanation of the code is contained within the analysis.py file itself.

The code contains the creation of:
- A modified CSV file with shortened names for variables
- A summary text file including some calculations using the data within the dataset
- Multiple png files containing histograms of the variables showing the distribution of the dataset overall and colour coded per species and a larger figure containing a subplot showing the variables per species separately
- A png file show a scatter plot of each pair of variables

To have a concise view of code for the generation of the different files the order you will see the code here differs slightly to that in analysis.py. 

### Importing required libraries

![Importing libraries](Images_for_readme/image.png)

> ℹ️ *For more details on the libraries and information of the functions used within each libraries check the "[Libraries within python](#libraries-witin-python)" section*

### Reading in the data

![Reading in the data](Images_for_readme/image-9.png)

### Error handling for PNG files

One function reused throughout the code is the check_png_file_exists() function.  
This enables a error message to be returned to the user if the a filename for one of the generated plots is already existing

![Check PNG file](Images_for_readme/image-10.png)

The above function reads in the value passed for the PNG_filename variable allowing the functionality to be reused throughout the program for the creation of the multiple PNG files.  

The OS library is used to check if the path exists for the file and raises a FileExistsError in case the filename is present in the folder, which in turn triggers the except path of the code outside of the function.  

### Creating the summary file

First we'll take a look at the function created for the creation of the summary file write_summary_file().

![Create text file code](Images_for_readme/create_text_portrait2(1).png)

#### Definition of variables and main text created for the text file

In the above, the FILENAME is first defined to be used for the error handling in case the file is already existing when the program attempts to create it.  

Then the function attempts to follow the try path, here the file is created. Setting 'x' as the mode ensures that a FileExistsError is thrown is the file exists and will not amend or overwrite the file if it is already in the folder. If this happens the program will jump to the except path and print a message for the user informing the file already exists.  

Within the step of creating the file the encoding is also set, UTF-8 is used to allow for symbols used in the table generated for the summary file to be saved to the text file.  

The following lines include the definition of numerous variables to use in the intro file. This intro which includes the main bulk of text and a mathematical summary of the variables is then written to the text file. Next the program moves to code calculating the correlation coefficient and displaying it for the user in an easy to read view as a table.  

#### Calculation of the correlation coefficient

An empty dictionary is created to later store the calculated correlation of the pairs of variables. A dictionary called "dfs_to_use" and a list called "xy_values" are passed from outside the function for use in the calculation. These are used to create a loop to allow the correlation for the relevant pairs of variables to be generated dynamically using values passed from the list and dictionary, removing the need for repeated lines of code with the variables hardcoded.  

The parent for loop passes over the different classes contained in the dfs_to_use, this allows the calculation of the correlation overall using the dates in the entire dataset for all classes and then calculate it for the individual classes. Within the classes for loop another for loop is used to iterate through the xy_value list. enumerate is then used to take the values from the tuples contained in the list and parse them to the variables x_value and y_value, it also starts the value the counter of the loop (i) to 1. 

Next an if statement is set so that the calculation is only carried out for certain iterations of the loop. This is to avoid carrying out the same calculations more than necessary as the list is used also for the generation of the scatter chart and contains blank "empty" tuples and the same variables twice with the order swapped (i.e. ('sepal width', 'sepal length') and ('sepal length', 'sepal width')).  

When the if statement condition is met, it is executed and the correlation is calculated using the class defined in the parent "for" loop and the x and y value defined in the second for loop. The name is then created using these values to allow for us to index into the dictionary when creating the table. The name and calculated correlation are then saved as a keypair to the correlations dictionary.

#### Creation of the correlation coefficient table

After all calculations are completed a list is created called "table" which contains 5 sub-lists, you can think of each list as representing a row in a table.   

The first row will be used to set the headers for the table using the string values it contains. The second list contains the values for the calculated coefficient for the entire dataset. The third list calls the data for relevant correlation values for the Setosa only, followed by the Versicolour list fourth and lastly the values for the Virginica class in the fifth list. The name of the keypair is used to index into the "correlations" dictionary and retrieve the value for the corresponding correlation.  

The tabulate library is then used to take the "table" list and format it as a table, it is set to consider the first row to be headers and the fancy grid option for the formatting is used to make it more pleasant to read the table. The table is then written to the summary file and the code for writing the summary file within the function is finished.

#### Looking at the lines within the main program of the code

![Summary code in main block](Images_for_readme/create_text_portrait2(2).png)

To make the program easily readable for the user the main code block outside of the function is minimum, for the creation of the summary file the relevant components in the main code block can be seen above. 
1. The xy_value list - used to set the variables which should be used for calculating the correlation coefficient
1. The dfs_to_use dictionary - used for selecting which data to use in the correlation calculations using first the data for the entire dataset and then separating the entries depending on class.
1. Line triggering the write summary file - this calls the function to be initiated and passes the list and dictionary to the function to be used within the function itself. 

### Creating Histograms
***

The creation .png files showing the distribution of each variable via a histograms is the next functionality we'll go through.

![Create_histograms](Images_for_readme/create_hist_portrait1(1).png)

The function uses the keypair values from the variable_and_filenames dictionary.  

A for loop is used to iterate over the keypairs in the dictionary reducing unnecessary repetition of lines of code. The try path is first attempted, if the check_png_file_exists() function (explained earlier in the notebook) returns a FileExistsError the except path will be triggered. The size of the figure for the png file is set to allow for the image to be large enough to comfortably fit the data in the image in an easily readable way.

Next the creation of two plots is triggered, first a plot showing the data for the variable in a given loop within the entire dataset, this is then plotted to the subplot in the first position. 

Next the histogram is created again for the subplot in the second position however this time the data is separated and colour coded per class of Iris to visualise the spread of distribution depending on the class for the variable. This is done using the "stacked" attribute to allow the data to be stacked on top of each other instead of treated as seperate columns. 

#### Customizing the histograms

Along with the figure size being set, there are various settings defined for customizing the appearance of the histogram.
The colour to be used for plotting the data per class is defined, the yticks are removed from the second subplot to avoid overcrowding of the figure as subplot 2 using the same range as the first subplot.  An overall title detailing the variable which is being plotted is added and the font side and position set. A shared label for the x axis is created using figtext since the plots share the same variable, the style, size and position of the text is defined. 

Lastly the file is saved using the filename passed in from the dictionary and ensuring no data like the title is cut off using the bbox_inches attribute. A message is then printed to the user to inform them that the file has been created and providing the filename.

#### Looking at the lines within the main block of code

![hist_code_in_main](Images_for_readme/create_hist_portrait1(2).png)

To make the program easily readable for the user the main code block outside of the function is minimum, for the creation of the histogram file the relevant components in the main code block can be seen above. 
1. The variables_and_filenames dictionary - used for passing the variable to plot in a loop to the function and the related filename to use when saving the figures.
1. Line triggering the create_histograms() function - this calls the function to be initiated and passes the dictionary to the function to be used within the function itself. 

### Creating the scatter plot
***

![scatter_funct](Images_for_readme/create_scatter_landscape1.png)
![scatter_funct_continued](Images_for_readme/create_scatter_landscape2(1).png)


The function uses the tuples from the xy_value list to generate a figure containing 16 subplots.

The try path is first attempted, using check_png_file_exists() function (explained earlier in the notebook) again, if it returns a FileExistsError the except path will be triggered. The filename and size of the figure for the png file is set to allow for the image to be large enough to comfortably fit the data in the image in an easily readable way to avoid potential overlap and ensure the plots are readable and not too small considering a large number of subplots are required to fit in the final figure.  

#### Looping over the values to be used for x and y
A for loop is also used in this function to iterate over the tuples in the list to reduce excess lines of code, setting the corresponding information in the tuple as the x and y value to be used in the plots, a counter is created as "i" with a starting value of 1 to allow the counter to be used to dynamically set the position of the subplot for each iteration later. 

#### Creating empty plots & condition for saving the figure
An if statement checks if the iteration is matching one of the numbers in the condition, if it does the corresponding plots will not contain a scatter plot but instead an empty plot is generated. The figtext method is used to position the name of a variable within the boundaries of the empty plot, this is to reflect which variable is being used for the x axis in a column and the y axis in the row where that plot is located.  

It also contains the logic to identify if the loop is in the last iteration to ensure the file is saved and the relevant steps which are only required to be completed once at the end are triggered. This includes the creation and positioning of the legend, the creation of the title for the figure and ensuring the layout is not overlapping. A message is also printed for the user at this stage in the loop to confirm the creation of the scatter plot .png file. 

#### Creating subplots containing the scatter plot of each pair of variables
The main else block contains the path all other iterations should take which involves actually creating scatterplots using the values contained in the tuples in the xy_value list. This block also includes a check for which class is being plotted and setting the corresponding colour depending on the class. 

An if statement is also used to ensure that the data for the dataset as a whole is not plotted as the goal is to show the scatter plot with colours indicating which class is linked to each marker on the plot. If any of the individual classes are used for the iteration is it trigger the line of code responsible the creation of the scatter plot, the line is dynamic using the value for the class_df from the dfs_to_use diction and the x and y values are select using the tuples in the xy_value list for each iteration. 

#### Customization of x and y ticks for specific subplots
As the requirements for customization of the plots varies depending on which position the subplot is located, a series of if elif statements are used to enhance the settings for the subplots depending on the iteration/subplot using the value of "i". The majority of the subplots require the removal of the x and y ticks, this is handled by the first if statement. 

The next 5 elif statements contain the ability to remove the x or y ticks or move the x or y ticks depending on what is required for the plot. For example for the subplot in position 4, the x and y ticks are set to be placed on the opposite side of the plot. Instead of the x labels and ticks being on the bottom of the plot as per the default, they are set to be moved to the top of the plot. Similarly for the y axis the y labels and ticks are set to be placed on the right of the plot instead of the left. This is done to reflect that the same range is used for all of the values in that column and y values in the row, in the end aiming to reduce clutter in the image and make the plot easier to read for the user. 

#### Looking at the main block of code

![scatter_main_block](Images_for_readme/create_scatter_landscape2(2).png)

To make the program easily readable for the user the main code block outside of the function is minimum, for the creation of the scatter plot file the relavant components in the main code block can be seen above. 
1. The xy_value list - used to set the variables for the x and y axis of each subplot depending on the iteration of the parent for loop within the function
1. The dfs_to_use dictionary - used for selecting which data to use in creation of the scatter plots, these values are also used for selecting the colour to be used in the loop for each class.
1. Line triggering the create_scatter_all_variables() - this calls the function to be initiated and passes the list and dictionary to the function to be used within the function itself.

### Creating figure containing histograms of each variable isolated per species

![hist_all_pt1](Images_for_readme/create_hist_all_portrait1(1).png)
![hist_all_pt2](Images_for_readme/create_hist_all_portrait1(2).png)

Likewise with the other plots, a check is done to ensure the file is not already existing and informing the user if this is the case.  
If the file is not existing already, the program continues the try path.  

The size for the overall figure is first set outside of the loop as we want all subplots within the same png file.  
A counter s is defined, this will be used to dynamically set the value for the subplot position in the figure.  

Next a for loop is defined with the purpose of cycling through the variables in the variable and filename dictionary. 

#### Setting the bin width 
In order to have the width of the bins in the histograms consistent for each of the classes individual histogram per variable, a function gets the minimum value in the dataset for a variable and sets that as the min width.  
The same approach is carried out to find the max value, these two numbers are then used to generate an array of evenly spaced numbers using NumPy's linespace function.  
This is then used to set the bin width for all histograms for that variable, when the loop changes to the next variable, the min and max value will be recalculated to get the appropriate range again for the columns width for the next iteration of the function.

#### Customization of the histograms
After the set_bins_width() function is completed it returns that values to be used in the parent function.

The next steps involves a for loop taking the values from the dfs_to_use list and sets them to the variables class_name and class_df.  
The class_df is then used to determine which class of data is represented in the plot.  
The first item in the dfs_to_use list contains the entire unfiltered dataset, which we do not want to plot.   
With this and if statement checks to ensure the plotting is only carried out for the other items in the list. 

Depending on which subplot is being generated we set the colour to be used for the bins, either remove the y ticks or move them to the right hand side of the plot positioned in the last row of each column. A label is also added in these loops to show which variable is being plotted in the rows.  
The title field is used to create a line break in between the rows to visualise the separation of the variables.

#### Setting y axis range
Next they y axis limits are set for the row of plots, a function sets the limits for the y range depending on the variable. i.e. all subplot in row 1 have the same y range defined so you can see the height of the columns and compare to the other subplots for the same variable.

In this function the min for y axis is set to 0 for all plots in the figure. An if statement branches out to decide what the max should be for the axis depending on the subplot being created using the value for the iteration counter. 

The y axis range is then set for the respective variable.  

#### Plotting the histograms
After the y range is set to histogram has all needed information for the subplot to be created.  
The data to be used is pulled from the class_df for the iteration, the variable to plot is passed in from the first for loop, the bins are set using the returned value from the set_bins_width() function and the colour is chosen depending on the subplot in question. 

At the end of the if statement the value for s is updated to allow it to be used as the value for the next subplot.  
This loop continues until the 12 subplot is generated, at this point the required steps which should only be done once or at the very last step are completed.  
The title is added using the font size chosen and the position set for the y axis. 
The legend is generated and font size chosen. Using the "loc"  and "bbox_to_anchor" attributes the position for the legend in this figure is set, being displayed at the very top of the figure just under the title since it is relevant for all plots in the figure. The legend is also customized to have 3 columns, with one class key shown in each column.

The file is then saved and the user is informed the file has been created using the value set as the PNG_filename at the beginning of the function.

#### Looking at the main block of code

![hist_all_main_block](Images_for_readme/create_hist_all_portrait1(3).png)

To make the program easily readable for the user the main code block outside of the function is minimum, for the creation of the scatter plot file the relevant components in the main code block can be seen above. 
1. The dfs_to_use dictionary - used for selecting which data to use in creation of the scatter plots, these values are also used for selecting the colour to be used in the loop for each class.
1. The variables_and_filenames dictionary - used for passing the variable to plot in a loop to the function when creating the subplots.
1. Line triggering the create_scatter_all_variables() - this calls the function to be initiated and passes the list and dictionary to the function to be used within the function itself.

## Analysis of findings from analysis.py
***

Ideas for what to include for analysis :

- Break down per  variables per class of Iris? maybe too much information and not needed
- Calculated correlation of: each pair of variables in the dataset maybe add then into scatter chart somehow?
- discussion on standard deviation for the histograms. 

### Correlation between variables 

![calculated_correlation_table](Images_for_readme/Correlation_table.png)

#### Overall dataset:
When looking at the calculated correlation between the variables using the entire dataset we can see that some pairs of variables appear to be strongly linked. 

**Variables showing strong positive correlation**
- Petal Length vs Sepal Length: 0.871754    
- Petal Width vs Sepal Length: 0.817954   
- Petal Width vs Petal Length: 0.962757  

The results of the correlation coefficient for the 3 pairs of variables listed above indicate a strong positive, when one variable in a pair increases the other is likely to increase as well.  
The Petal Width vs Petal Length pairing appears to be a near perfect linear positive correlation of 0.962757.

**Variables showing a moderate negative correlation**
- Petal Length vs Sepal Width: -0.420516   

For the pair above there is a moderate negative correlation, the correlation is not as strong as the previously discussed pairings.  
We also see that the direction of the relation is negative, negative relations in theory would indicate that when one variable increases the other is actually likely to decrease.  
While the correlation is still a significant enough amount to indicate some relationship between the pairings it is not as reliable. 

**Variable showing a weak or very weak negative correlation**
- Petal Width vs Sepal Width: -0.356544  
- Sepal Width vs Sepal Length: -0.0109369  

When looking at the sepal width vs sepal length we can see this is the weakest of the correlations when look at the dataset as a whole.  
The result is indicating an extremely week negative relationship between the two and it could not be assumed that as variable increases the would decrease in a proportionate way.  

Next we'll factor in the class of Iris to see if the correlation between the variables differs depending on the class.


#### Breakdown per species:

##### *Setosa*

**Variables showing strong positive correlation**
- Sepal Width vs Sepal Length: 0.74678 

**Variable showing a weak or very weak negative correlation**
- Petal Width vs Petal Length: 0.306308
- Petal Width vs Sepal Width: 0.279973
- Petal Width vs Sepal Length: 0.279092
- Petal Length vs Sepal Length: 0.263874
- Petal Length vs Sepal Width: 0.176695

##### *Versicolor*

**Variables showing strong positive correlation**
- Petal Width vs Petal Length: 0.786668  
- Petal Length vs Sepal Length: 0.754049  

**Variables showing a moderate positive correlation**
- Petal Width vs Sepal Width: 0.663999
- Petal Length vs Sepal Width: 0.560522
- Petal Width vs Sepal Length: 0.546461
- Sepal Width vs Sepal Length: 0.525911

##### *Virginica*

**Variables showing strong positive correlation**
- Petal Length vs Sepal Length: 0.864225  

**Variables showing a moderate positive correlation**
- Petal Width vs Sepal Width: 0.537728  
- Sepal Width vs Sepal Length: 0.457228
- Petal Length vs Sepal Width: 0.401045  

**Variable showing a weak or very weak positive correlation**
- Petal Width vs Petal Length: 0.322108  
- Petal Width vs Sepal Length: 0.281108  


**Observations from correlation table**

Interesting to observe the different in correlation between the classes of Iris for a pair of variables and that when the 3rd factor of the class is added you see very different results in the correlation between the variables. 

For example when we look at the Petal Width vs Petal Length overall we see a near perfect positive correlation of 0.962757.  
However, when we look across the class we see Setosa (0.306308) and Virginica (0.322108) have a much weaker correlation compared to when looking at the values for all species as one.  

Likewise with with Petal Length vs Sepal Width overall we see that there is a moderate negative correlation across the dataset (-0.420516). 
In contrast when we look at the individual classes, none of the classes suggest a negative relationship between the petal length vs sepal width when the data for a class is separated. In fact when looking at Virginica and Versicolor as individual groups of data we can see that they have a moderate positive correlation between the variables. 

Another example which highlights the difference once taking the class into consideration is the Sepal Width and Sepal Length. Looking at the calculation for the overall dataset you would assume that there is very weak negative correlation between the pair of variables throughout the dataset. However, when we look at the individual classes we see that actually all relationships indicate a moderate - strong positive relationship between the variables.

We can also see that each class of Iris has its pattern and relationship between the classes, indicating that the class of species has a big effect on the petal and sepal sizes. 

This highlights the importance of understanding the complexity of the data in the dataset and the importance of considering underlying factors when interpreting the results.  
If we were to base our understand of the correlation of the variables bases solely on the calculated correlation of the overall dataset combined it would be very easy to reach some incorrect conclusions.

#### Scatter plot analysis: 

![Scatterplot](Images_for_readme/scatter_all_variables.png)

Looking at the scatter plot above we can make some interesting observation. 

Setosa appears to be more of an outlier and the easiest of the classes to distinguish using the characteristics of the sepal and petal, with Versicolor and Virginica being more closely grouped across all plots.

If trying to use the data to distinguish between the different classes the Sepal length vs Sepal width would be the most overlap of the Versicolor and Virginica markers on the plot. The wide spread for the variables also shows us that there is a lot of variety in the ranges in this pairing.  

In contrast the Petal length vs petal width may be a better candidate to use as we see the class markers overlapping less and the data more tightly clustered together on the x and y axis.

From the plots we can also see that of the classes, the Virginica class tends to have the widest and longest petals, with Setosa being much smaller in these respects.  

#### Histogram analysis

![hist_overall_sum](Images_for_readme/hist_variables_overview.png)

Looking at the variables plotted for the dataset the data seems quite spread out.  

For petal width and sepal length the histogram appears to be multimodal with more than 1/2 peaks.  
For petal length the histogram appears to be bimodal with two distinct peaks.  
Then for sepal width this histogram appears to be unimodal.  

Next we'll take a look at the histograms when the class of Iris is considered:

![hist_class_included](Images_for_readme/hist_class_included.png)

##### Petal length

![image-4.png](attachment:image-4.png)  
![image-2.png](attachment:image-2.png)

Setosa - very separated from the rest. Strong grouping between 1 - 1.5 (cm).  
Versicolor - 0.469911 standard deviation relatively narrow range of deviation. 
Histogram is not unimodal or symmetric. 3 peaks.

### Additional resources/reading:
***
Adding screenshots to Jupyter notebook
https://medium.com/@yogeshkd/four-ways-to-embed-images-in-your-jupyter-notebook-powered-blog-2d28f6d1b6e6#:~:text=1.,command%20to%20embed%20the%20screenshot.

https://en.wikipedia.org/wiki/Iris_flower_data_set  
https://www.markdownguide.org/hacks/  
https://www.kaggle.com/datasets/uciml/iris  
https://archive.ics.uci.edu/dataset/53/iris  
https://matplotlib.org/2.0.2/api/markers_api.html  
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html  
https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html  
https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html  
https://www.geeksforgeeks.org/create-a-stacked-bar-plot-in-matplotlib/  
https://www.pythoncharts.com/matplotlib/histograms/#:~:text=The%20histogram%20bars%20have%20no,some%20separation%20between%20the%20bar.&text=An%20alternative%20is%20just%20to%20make%20the%20bars%20skinnier%20using%20rwidth%20.  
https://matplotlib.org/stable/users/explain/colors/colors.html  
https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d  
https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.clf.html#matplotlib-pyplot-clf   
https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.suptitle.html  
https://www.geeksforgeeks.org/matplotlib-pyplot-suptitle-function-in-python/  

https://www.simplilearn.com/tutorials/python-tutorial/enumerate-in-python
https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/  
https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/


https://www.w3schools.com/python/ref_dictionary_items.asp
https://www.geeksforgeeks.org/python-dictionary-items-method/
https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects

Inspiration for format of the scatter plot https://en.wikipedia.org/wiki/Iris_flower_data_set#/media/File:Iris_dataset_scatterplot.svg
     
## Libraries within python
***

Within the program we are importing various external libraries and classes to use throughout the notebook including: 
- Pandas
- Matplotlib.pyplot
- NumPy
- Tabulate

#### Pandas:
Pandas[^] is a library in Python used for data analysis which enables the use of two-dimensional tables called DataFrames.  
Within the *analysis.py* file the Pandas library is used to read in the data from the Iris dataset.  
The following are some methods used throughout the project from Pandas: 
> .corr - used for calculating the correlation coefficient of the variables flipper length and body mass in the dataset.[^]

> .unstack - used with the groups created with groupby() to arrange them in an organised manner. This allows us to create a stacked bar chart to visualise the data of the species per island.[^] 

> .std - used to calculate the standard deviation in the dataset to determine the spread of the values for a variable from the mean. [^]

#### Matplotlib.pyplot:
The Matplotlib.pyplot library is used mainly for visual representation of the dataset.
This library enables the creation of many types of plots including bar charts, histograms and scatter plot which are generated by the *analysis.py* file.  
There is a high level of customisation possible with options to switch up the colour,[^] markers,[^] labels and titles of the plots.

The following are some methods used throughout the notebook from Matplotlib.pyplot: 

> .scatter - creates scatter plots to visualise the relationship between two variables by plotting markers on a graph where each marker represents an entry in the dataset.[^]

> .plot - used in the *analysis.py* to create empty plots as placeholders for text containing the variable names to be used for the scatter figure. [^]

> .hist - creates histogram to represent distribution of values for a variable in the dataset.[^]

> .subplot - supports the creation of multiple plots in one figure. The number of plots which can be displayed is controlled by values entered for the number of columns and rows required. 

> .xticks & .yticks - offers the ability to change the default tick settings on the x and y axes including the possibility to change the position of the ticks on the plot borders or remove the ticks completely.[^]

> .xlabel & .ylabel - sets the heading for the axes and allows customisation of the font with the possibility to change the style, font and location of the labels. [^] 

> .ylim - used for setting the limit of the y axis. This is useful when it's needed to overwrite the default value or range for the axes. [^]

> .figtext - used for adding text to plots. In *analysis.py* it is used to set super-labels to axes which have a common variable to make the figure less cluttered and easier to read. [^]

> .figure - is used in *analysis.py* to adjust the size of the figure, to ensure that figures with multiple plots are not overcrowded or distorted and difficult to read. [^]

#### NumPy
NumPy is used in the *analysis.py* file to facilitate calculations on the large amount of data.  When working with datasets NumPy is useful for its ability to handle arrays and possibility to complete mathematical calculation and sorting.[^]

> .linspace - used to generate a NumPy array of evenly spaced numbers between a min and max value, the amount of numbers to be included is customizable.

#### Tabulate
Tabulate makes it possible to create formatted tables to present data from DataFrames and lists in a clear and concise way.  
The table's appearance is customisable, with options to configure if the table has headers and if there are borders between the cells. [^]

### Python core functionality: 

In addition to the above functionality from the imported libraries, there is two honourable mentions for functionality within the standard Python environment which are key for the *analysis.py* file. 

> enumerate() - Works as a way to loop over objects while also keeping count for the loop. Makes it possible to work with dictionaries key-pairs when used with the items() method. The function takes in two arguments, the sequence to be used for the loop and optionally the starting value for the loop. Using indexing enumerate adds the possibility to access key-pair information from a dictionary, this makes it possible to change values in the loop after each iteration.   
In the case of analysis.py file it allows for the variable to be used to plot the histogram and the filename of the png to be updated after each iteration resulting in much neater code.  It is also used for the creation of the scatter plot to enable loops to be used to avoid unnecessary repetition of code by iterating over the different combinations of variables to compare and plot.  

> items() - Returns a view option that contains key-pair values in from a dictionary.   
For *analysis.py* it is pulling the variable and png filename to be used with the enumerate function for the histogram loop.  It is also used to pull the information of the class name and respective filtered information from the dataset for the scatter plot and the large histogram of all variables separated per species.

#### Next actions/To-do list:
- ~~Create all code needed in this notebook first to enable easy checking of batches of code~~
- ~~Decide if README will be a jupyter notebook or just .md file (Does readme file just get deleted if using Jupyter notebook?)~~
- ~~Last review of code & generated plot to see if any further tidying up is needed~~
- ~~Decide > do I want to include the calculation of standard deviation into the large figure with subplot of each of the variables in the image > no too crowded~~
- Explanation of code: 
    - ~~Decide if using screenshot or code directly in the notebook (if using notebook figure out how the code may need to be adjusted i.e. not saving the images when running the cells) > code directly~~
    - ~~Create files of the different functionality separated to have all the related functions and code in one cell/screenshot~~
    - ~~Remove comments from individual functionality files to make it easier to read to give high level explanation~~ 
    - ~~Mention that line by line explanation of code is within the .py file~~
- Start adding analysis and observation to the notebook.ipynb
- Add extra analysis and commentary to accompany the plots in notebook
- Add sources to notebook and any research/readings done for the project

### python file:
- ~~Update python file after piece of code is validated~~
    - ~~Add code which outputs a summary of each variable to single text file > point to consider: should I add breakdown information per species of the summary?~~ 
    - ~~Add code to create histograms of each variables to png files~~
    - ~~Add code to create s scatter plot of each pair of variables~~

- ~~Create subplot which shows all variables against each other~~

- ~~Ideas for improvement of the scatter plot:~~
    - ~~Investigate if there is a way to make the variables to plot on x and y axis dynamic like with the histogram function created above using loop and enumerate~~
    - ~~Think about how to handle customization:~~
        - ~~Use if/elif/else in the loop to decide which customization to use depending on the subplot being plotted~~  
            ~~i.e. if i=1 or 6 or 11 or 14 plot empty subplot so figtext can be added later for the variables~~  
                ~~elif i=3,7,8,9,10,12 remove x and y ticks etc~~  
    - ~~If I can get that working need to decide how to structure the main code, do I have functionality to create scatter in a function and use function within a function?~~

- ~~Create histogram of each variable:~~  
    - ~~Write code first which generates the histograms for each variable~~
    - ~~Point to consider: Would it be interesting to created stacked histogram of the variables showing variables for the different species~~
    - ~~Point to consider: Addition file showing subplot that would have 4 rows, 3 columns in each and show the individual histograms per class~~
    - ~~Refactor code to make the final histogram plots neater.~~  
    
- ~~Enhance so that histograms are saved to seperate png files~~

- ~~- Additional calculations:~~  
    -  ~~Point to consider: Would it be interesting to include the calculations of correlation, standard deviation?~~  
    - ~~Brainstorm any other insightful calculations that could be included~~

- ~~Point to consider: Would it be a good idea to include error handling to first see if the file is already created and if so displaying a message to the user like "Filenames already existing in folder, no new files generated."~~

- Spellcheck

### README.md sections:

- Research & summary of dataset  
- ~~How to run code~~
- ~~Cloning & Pulling GitHub~~
- ~~Running on your machine~~
- Explanation of what code does > in progress - need to be completed for large figure with histogram subplots. (Also think about adding more detail for the intro file like what the summary actually contains not just "numerical data")
- Analysis of own findings (including comparison to findings of published studies or analysis online from others)
- Footnotes & additional reading section
- Refactor notebook 
    - Spellcheck
    - Enhance formatting to break down large chunks of text (maybe adding more sub-headings in the explanation of the code would help)

***
## End
