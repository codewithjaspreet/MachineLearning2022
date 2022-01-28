import pandas as pd
import os

print(os.getcwd())  # for getting directory working in

df = pd.read_csv('example.csv', index_col=0)
print(df)
# df.to_csv('location to save' ,index=False)
