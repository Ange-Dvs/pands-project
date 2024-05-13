#importing the libaries to use in the program
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv('modified_iris_data.csv') 

def check_png_file_exists(PNG_filenames): 
    if os.path.exists(PNG_filenames): 
        raise FileExistsError 

def setting_axis_limits(s): 
    ymin = 0 
    if s in (1, 2, 3):
        ymax = 19.5
    elif s in (4, 5, 6):
        ymax = 16.5
    elif s in (7, 8, 9):
        ymax = 38
    elif s in (10, 11, 12):
        ymax = 42
    plt.ylim(ymin, ymax)

def set_bins_width(variable_to_plot, dfs_to_use):
        min_width = min(df[variable_to_plot].min() for df in dfs_to_use.values()) 
        max_width = max(df[variable_to_plot].max() for df in dfs_to_use.values()) 
        bin_edges = np.linspace(min_width, max_width, 11) 
        return bin_edges 

def create_histogram_per_classes(variables_and_filenames, dfs_to_use):
        PNG_filenames = 'hist_all_variables_per_species.png' 
        try: 
                check_png_file_exists(PNG_filenames) 
                plt.figure(figsize=(9, 14)) 
                for variable_to_plot in variables_and_filenames: 
                        bin_edges = set_bins_width(variable_to_plot, dfs_to_use) 
                        for i, (class_name, class_df) in enumerate(dfs_to_use.items(), start=1): 
                                if i != 1: 
                                        plt.subplot(4, 3, s) 
                                        if s in (1, 4, 7, 10): 
                                                colour_to_use = 'violet'
                                                plt.yticks([])
                                        elif s in (2, 5, 8, 11): 
                                                colour_to_use = 'navy' 
                                                plt.yticks([]) 
                                                plt.xlabel(f'{variable_to_plot} in (cm)', fontsize=20) 
                                        else: 
                                                colour_to_use = 'orange' 
                                                plt.tick_params(axis='y', direction='out', right=True, labelright=True, left=False,
                                                                labelleft=False) 
                                        plt.title('--------------------------', fontsize=20) 
                                        setting_axis_limits(s) 
                                        plt.hist(class_df[variable_to_plot], bins=bin_edges, color=colour_to_use) 
                                        if s == 12: 
                                                plt.tight_layout()
                                                plt.suptitle('Histograms per class', y=1.075, fontsize=32) 
                                                plt.figlegend(loc='upper center', ncols=3, bbox_to_anchor=(0.5, 1.035), fontsize=14,
                                                        labels=['Setosa', 'Versicolor', 'Virginica']) 
                                                plt.savefig(PNG_filenames, bbox_inches='tight') 
                                                print(f'{PNG_filenames} created.\n') 
                                        s += 1 
        except FileExistsError:
                print(f'\nError: Filename {PNG_filenames} already exists in folder.\n')

dfs_to_use = {'All classes -': df,'Setosa -': df[df['class'] == 'Iris-setosa'], 'Versicolor -': df[df['class'] == 'Iris-versicolor'], 'Virginica -': df[df['class'] == 'Iris-virginica']} 

variables_and_filenames = {
    'sepal length': 'hist_sepal_length.png',
    'sepal width': 'hist_sepal_width.png',
    'petal length': 'hist_petal_length.png',
    'petal width': 'hist_petal_width.png'}

create_histogram_per_classes(variables_and_filenames, dfs_to_use)

