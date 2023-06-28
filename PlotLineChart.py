'''
Write a python program to plot a line chart using following information.
Date =[17/10,18/10,19/10,20/10,21/10,22/10,23/10,24/10,25/10]
Temperature=[25,26,25.5,24,23.7,26.8,28,30.2,31]
a)	Plot a line chart of date versus temperature
b)	Line color should be blue
c)	Line width should be 0.5
d)	Line style should be dotted
e)	Add labels on X & Y axis
f)	Add title to the chart
g)	Add grid to the chart
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
date=np.array([17,18,19,20,21,22,23,24,25])
temperature=np.array([25,26,25.5,24,23.7,26.8,28,30.2,31])
plt.plot(date,temperature,linestyle="dotted",color="blue",linewidth="0.5")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Date vs Temperature")
plt.grid()
plt.show()
