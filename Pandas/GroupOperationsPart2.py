import numpy as np
import pandas as pd

df = pd.read_csv('mpg.csv')

year_cyl = df.groupby(['model_year', 'cylinders']).mean()
print(year_cyl)
# print(df.group(['model_year', 'cylinders']).mean().index)
print(year_cyl.loc[(70, 4)])

# .xs method

print(year_cyl.xs(key=70, level='model_year'))  # cross-section

# xs is good from inner index

print(year_cyl.xs(key=4, level='cylinders'))
# can only put one value for key


# first filter dataframe then call group makes task easier
# for example if u want to grab for 6 & 8 cylinders for each year

ans = df[df['cylinders'].isin([6, 8])].groupby(['model_year', 'cylinders']).mean()
print(ans)

# swap levels

# year_cyl.swap level()  # swap cylinders to model_year & vice-versa

# sorting

# year_cyl.sort_index(level='mode_year', ascending=False)
# makes sense for outer levels

print(df.agg(['std', 'mean'])['mpg'])

print(df.agg({'mpg': ['max', 'mean'], 'weight': ['mean', 'std']}))
#  advanced application of aggregate function to different individual columns
