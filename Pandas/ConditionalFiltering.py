import numpy as np
import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({'Year': [1776, 1867, 1821],
                   'Pop': [328, 38, 236, ],
                   'GDP': [20.5, 1.7, 1.22]})

idx = ['USA', 'CANADA', 'MEXICO']
df.index = idx
print(df)
print(df['Pop'] > 50)  # perform conditional filtering
print(df[df['Pop'] > 50])  # make changes in original dataframe

# multiple conditional filterings

# and  - >  both conditions need to be true
# or - > either of the conditions
print(df[(df['Year'] > 1868) & (df['Pop'] > 100)])
#  | pipe operator for or

options = [20.5 , 1.22]

print(df[df['GDP'].isin(options)])
# isin method faster way of checking two or more conditions


