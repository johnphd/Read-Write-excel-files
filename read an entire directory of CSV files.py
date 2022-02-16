# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:59:18 2022
One resource https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe
@author: John PhD (Zoro Code)
"""

# import necessary libraries
import pandas as pd
import os
import glob
  
  
# use glob to get all the csv files 
# in the folder

path=r"C:\Temp\Old stuff\Graduate School\Research\Ceramics Project\EIS Data\Permittivity"  # sets file path
os.chdir(path)                                                  #this tells python to change working directory to file path

path = os.getcwd()

csv_files = glob.glob(os.path.join(path, "*.csv"))              # this tells python to read all the csv files in a folder
  

                                                                    
    # read the csv file
cols=[4,10,11,12,13]                                              #the columns we went to load  Ideally there are 4 columns, but may be more if data files are different

                                                                # this creates a dataframe of the csv files, and contains a loop statement
                                                                # and sets the header to line n.  Here n=2 but might 
                                                                # change for each file, some trial and error here.

df=pd.concat((pd.read_csv(f, usecols=cols,low_memory=True, header=2) for f in csv_files))     

col_names='header'
    
cols=df.columns                                 # loads the column names if you want to see them. Time cost is minimal.

      
                                                # print the content
print('Content:')
print(df)                                      #optional
#  print(cols) will display the column names   # optional
#  print()