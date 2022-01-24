import numpy as np

arr = np.arange(0, 10)

arr + 5  # applied on all values
arr - 2  # applied on all values

arr + arr  # applied on all values
arr * arr  # applied on all values

arr / arr  # in case of  0/0 it replaces to 'nan' & in 1/0 replaces with 'inf'  but gives warning

np.sqrt(arr)

np.sin(arr)

np.log(arr)

#
# .
# .
# .
# lots of method

arr.sum()
arr.max()
arr.var()
arr.std()
arr.var()

# in case of 2d array

arr2d = np.arange(0, 25).reshape(5, 5)
arr2d.sum()
print(arr2d.sum(axis=0))  # performs across the rows
print(arr2d.sum(axis=1))  # performs across the columns
