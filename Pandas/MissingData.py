import numpy as np
import pandas as pd

df = pd.read_csv('movie_scores.csv')
# Dealing with Missing Data


print(pd.NaT)

# conditional filtering using null & notnull methods
print(df.isnull())  # notnull() vice-versa
print(df[df['pre_movie_score'].notnull()])
print(df[(df['pre_movie_score'].isnull()) & (df['first_name'].notnull())])

# options
#  keep it
# Remove it
# Replace it
# print(help(df.dropna))
print('\n')
print(df.dropna())
print(df.dropna(thresh=1))
print(df.dropna(axis=1))
print(df.dropna(subset=['last_name']))

print(df.fillna('NEW_VALUE !'))  # fill in place where null

print(df['pre_movie_score'].fillna(0))
print(df['pre_movie_score'].fillna(df['pre_movie_score'].mean()))
print(df.fillna(df.mean()))

airline_tix = {'first':100,'business':np.nan,'economy-plus':50,'economy':30}
ser = pd.Series(airline_tix)
print(ser)
print(ser.interpolate())