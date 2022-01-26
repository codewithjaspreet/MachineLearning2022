import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({'Weight': [45, 88, 56, 15, 71],
                   'Name': ['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'],
                   'Age': [14, 25, 55, 8, 21]})

# Create the index
index_ = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5']

# df.ioc works on index based
# Set the index
df.index = index_

# Print the DataFrame
print(df)
# return the value
result = df.loc['Row_2', 'Name']

# Print the result
print(result)

print(df.loc[:, ['Weight', 'Age']])
# use DataFrame.loc attribute to return the values present in the ‘Weight’ and ‘Age’ column of the Dataframe.

print(df.drop('Row_1', axis=0))
print(df.iloc[2 :])

# add new row
one_row = df.iloc[0]
print(df.append(one_row))
