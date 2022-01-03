# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:49:43 2021

@author: Johnphd
This is code borrowed and pieced together from github.  It's a first trial for data plotting from familar file layouts..

"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#  this section is for each data file being read into python.  There is no limit I think
loc1 = r"C:\Temp\Matlab\practice\Data for figures (mishmash)\BiP (0.1M sodiated in G2) vs TEMPO (PB) Beta Al2O3\210508-2 END.xls" # full path

filename=Path(loc1).stem  # this removes the path (in loc1) from the filename
str_1=filename              #  Identifies 'filename'as a string

df = pd.concat(pd.read_excel(loc1, sheet_name=[3,4,5,6]), ignore_index=False)
df.shape

df['Absolute Time'] = pd.to_datetime(
    df['Absolute Time'],
    format='%m.%d.%Y %H:%M:%S.%f',
    errors='coerce')



origin = df['Absolute Time'].min()

df['Time(h)'] = (df['Absolute Time'] - origin).dt.total_seconds() / 3600

#  df.drop_duplicates(subset=['Absolute Time']) # this omits duplicate entries in the x axis (Time)

df.plot(x='Time(h)',y='Voltage(V)', color="red")#x="Time(h)",y="overpotential(V)")

plt.xlim(0,1000)       # sets x axis boundaries
plt.ylim(1.5,4)      # sets y axis boundaries

plt.xlabel("time (h)")   #  This is a specific value
plt.ylabel("voltage (V)")  
plt.title(str_1)        # filename is used in each sample as a graph title
plt.show()  
