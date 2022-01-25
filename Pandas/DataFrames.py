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
df = pd.read_csv('winequality-red.csv')



