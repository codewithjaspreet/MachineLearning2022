import numpy as np
import pandas as pd

# Concatenation
# can be on rows as well as columns
# after concat it fills Nan automaticaly where neccessary


data_one = {'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']}
data_two = {'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}

one = pd.DataFrame(data_one)
two = pd.DataFrame(data_two)
print(one)
print(two)
print(pd.concat([one, two, ], axis=1), )

two.columns = one.columns
print(pd.concat([one,two],axis=0)) # after copying names of columns this concat makes sense

mydf = pd.concat([one,two],axis=0)
mydf.index = range(len(mydf))
print(mydf)
