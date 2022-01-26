import numpy as np
import pandas as pd

df = pd.DataFrame({'points': [25.3, 12.2, 15.4, 14.5, 19.2, 23.6, 25.2, 29.5],
                   'assists': [5, 7, 7, 9, 12, 9, 9, 4],
                   'rebounds': [11, 8, 10, 6, 6, 5, 9, 12]})

print(df.columns.tolist())
myCol = ['points', 'assists']
print(df.head())
print(df[myCol])

# performing operations  columns like numpy arrays

df['new_col'] = df['points'] + df['assists']
print(df.head())

# if new column already exist it will override
print(df['points'] + df['assists'])

print(np.round(df['points'], 0))
# an example how we can use numpy universal functions with pandas since each column in pandas
# dataframe is  a series

print(df.drop('new_col', axis=1 ))  # removing columns
# axis  = 1  ->  columns , axis = 0 -> rows

# for permanently deletion of column
df = df.drop('new_col', axis=1)  # can use inplace but might depreciate


