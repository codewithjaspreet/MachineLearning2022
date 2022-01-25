# several series with same index

# each column is a separate pandas series

import numpy as np
import pandas as pd

np.random.seed(101)
myData = np.random.randint(0, 101, (4, 3))
print(myData)

myIndex = ['CA', 'NY', 'AZ', 'TX']
myColumns = ['Jan', 'Feb', 'Mar']
df = pd.DataFrame(myData, index=myIndex, columns=myColumns)
print(df)

print(df.info())

# read database from csv file
df1 = pd.read_csv('winequality-red.csv')

print(df1.columns)  # no of columns
print(df1.index)  # all columns info
print(df1.head(4))  # head for some starting rows
print(df1.tail(4))  # last rows

print(df1.info())  # all about the dataframe

print(df1.describe())
print(df1.describe().transpose())
