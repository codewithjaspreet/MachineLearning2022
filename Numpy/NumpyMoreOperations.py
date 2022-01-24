import numpy as np

arr = np.arange(0 , 10)

arr + 5   # applied on all values
arr - 2    # applied on all values

arr + arr  # applied on all values
arr * arr  # applied on all values


arr / arr  # in case of  0/0 it replaces to 'nan' & in 1/0 replaces with 'inf'  but gives warning


