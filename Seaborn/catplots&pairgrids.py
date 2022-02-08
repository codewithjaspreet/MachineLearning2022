# -*- coding: utf-8 -*-
"""CatPlots&PairGrids.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19dH5m95eT7RMb6agzO23aOVwLCCHsjS_
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('StudentsPerformance.csv')

a = df.head()



sns.catplot(data = df , x = 'gender' , y = 'math score' , kind ='box' ,col = 'lunch' , row ='race/ethnicity') # row somewhat same as hue with grid   # kind can be - box , voilin etc etc , catplot can call different plots a general method u can say

g = sns.PairGrid(df,hue='gender')
g

g = g.map_upper(sns.scatterplot)
g = g.map_diag(sns.histplot)

g = g.map_lower(sns.kdeplot)

g = g.add_legend()





















