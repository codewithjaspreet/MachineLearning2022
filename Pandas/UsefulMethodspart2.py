import numpy as np
import pandas as pd

df = pd.read_csv('tips.csv')

df.describe()

print(df.sort_values('tip'))
# ascending  = false  for descending
print(df.sort_values(['tip', 'size']))
#  can also sort for multiple columns


print(df['total_bill'].max())
print(df['total_bill'].idxmax())

print(df.iloc[170])

#  or in one line

print(df.iloc[df['total_bill'].idxmin()])

print(df.corr())  # correlation checks

# let's figure out how many males and female are there in the dataset

print(df['sex'].value_counts())

print(df['day'].unique())

# replace values

print(df['sex'].replace('Female', 'F'))
# also work with multiple replace values
# like  pass ['Female' , 'Male'] , ['F' , 'M']

myMap = {'Female': 'F', 'Male': 'M'}
df['sex'].map(myMap)  # better for lots of items

df.duplicated()  # this will return very first instance of duplicate

df.drop_duplicates()  # remove duplicate columns

print(df[df['total_bill'].between(10, 20, inclusive=True)])

# filter with between


print(df.nlargest(2, 'tip'))  # top 2 columns with max tips

# another way can be
print(df.sort_values('tip', ascending=False).iloc[0:2])

# similarly is  .nSmallest()

print(df.sample(5))  # return 5 random rows

print(df.sample(frac=0.1))  # return 10% of the data random
