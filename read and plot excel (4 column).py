# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:49:43 2021

@author: Johnphd
This is code borrowed and pieced together from github.  It's a first trial for data plotting from familar file layouts..
The source file here is an export from LANDT battery test systems, an excel sheet with four columns for 
time (in hours), current (miliamps), capacity (mAh), and overpotential (volts)
The idea here was to extract and plot the data relatively quickly.  On a side note I have spent countless hours in 
Origin doing this very thing.    It can be streamlined as well. 

file layout is like this in a single sheet excel:
    
    A          B           C           D
    hours      current     capacity    voltage 

"""


import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#  this section is for each data file being read into python.  There is no limit I think.  "r" is because I use irregular path/filenames
loc1 = r"C:\path\filename.xlsx"
#  loc2 = r"C:\path\filename2.xlsx"
#  subsequent files can also be loaded


#  FOR sample #1  I am not sure if this is required to be copied and pasted to each sample section, is there a shorter way?

x=pd.read_excel(loc1, usecols="A")   # Time in hours
g=pd.read_excel(loc1, usecols="B")   # current (mA)
g2=pd.read_excel(loc1, , usecols="C")  #Capacity (mAh)
g3=pd.read_excel(loc1, usecols="D")  #  overpotential (volts) 
           
filename=Path(loc1).stem  # this removes the path (in loc1) from the filename

str_1=filename            #  Identifies 'filename'as a string

#  This produces three different plots as shown                   
#  This is a voltage versus time plot
#  copy paste this section for each sample.  Not tidy and small, but functional

#df.set_index("time", drop=true, inplace=true)
plt.xlim(0,250)       # sets x axis boundaries
plt.ylim(0.5, 4)      # sets y axis boundaries
plt.plot(x,g3, color='blue')
plt.xlabel(x.columns.values[0])   #  This automatically takes the first value from column as 'x' axis title
plt.ylabel(g3.columns.values[0])  #  This automatically takes the first value from column as 'y' axis title
plt.title(str_1)        # filename is used in each sample as a graph title
plt.show()
#  left, right = xlim()  # return the current xlim


#  This is a time versus capacity plot
plt.xlim(0,250)
plt.plot(x,g2, color='red')
plt.xlabel(x.columns.values[0])
plt.ylabel(g2.columns.values[0])
plt.title(str_1)
plt.show()


# this is a potential versus capacity plot, scatter
plt.xlim(-0.1,2,5)
plt.ylim(0.5,4)
#  str.plot(style='*', figsize=(20,10), ms=2)
plt.scatter(g2,g3, color='black',marker='.', s=2)   #s is the data point size
plt.xlabel(g2.columns.values[0])
plt.ylabel(g3.columns.values[0])
plt.title(str_1)
plt.show()

print()    # these last line are optional,  just separators for the console window

print('----filename--completed-------------------------------------------')
