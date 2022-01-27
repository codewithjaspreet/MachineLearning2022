import numpy as np
import pandas as pd

df = pd.read_csv('mpg.csv')
print(df)
print(df.groupby('model_year').mean()['mpg'])
print(df.groupby(['model_year', 'cylinders']).mean()['mpg'])  # return multilevel index

print(df.groupby('model_year').describe().transpose())
print(df.groupby(['model_year', 'cylinders']).mean())

print(df.groupby(['model_year', 'cylinders']).mean().index)

year_cyl = df.groupby(['model_year', 'cylinders']).mean()
print(year_cyl)
print(year_cyl.index)
print(year_cyl.index.levels)
print(year_cyl.index.names)
print(year_cyl.loc[70])
print(year_cyl.loc[[70, 82]])  # works on outside level index

print(year_cyl.loc[(70, 4)])
