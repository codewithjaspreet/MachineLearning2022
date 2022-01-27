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

