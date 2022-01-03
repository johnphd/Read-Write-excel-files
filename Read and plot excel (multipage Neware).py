# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:49:43 2021

@author: Johnphd
This is code borrowed and pieced together from github.  It's a first trial for data plotting from familar file layouts..

"""

import pandas as pd
import matplotlib.pyplot as plt

#  this section is for each data file being read into python.  There is no limit I think
loc1 = r"drive:\path\file.xls" # full path

filename=Path(loc1).stem  # this removes the path (in loc1) from the filename
str_1=filename              #  Identifies 'filename'as a string

df = pd.concat(pd.read_excel(loc1, sheet_name=[3,4,5,6]), ignore_index=False) # sheetnumbers are manually entered, did not find a shortcut for this
df.shape                                                # concantenates multiple pages

df['Absolute Time'] = pd.to_datetime(   
    df['Absolute Time'],
    format='%m.%d.%Y %H:%M:%S.%f',
    errors='coerce')



origin = df['Absolute Time'].min()

df['Time(h)'] = (df['Absolute Time'] - origin).dt.total_seconds() / 3600   # converts columns of time stamps to hours

df.plot(x='Time(h)',y='Voltage(V)', color="red")#x="Time(h)",y="overpotential(V)") # using column headers, sets x,y data and plot

plt.xlim(0,1000)       # sets x axis boundaries
plt.ylim(1.5,4)      # sets y axis boundaries

plt.xlabel("time (h)")   #  explicite label for x and y axes.
plt.ylabel("voltage (V)")  
plt.title(str_1)        # filename is used in each sample as a graph title, helps when there are hundreds of graphs
plt.show()  
