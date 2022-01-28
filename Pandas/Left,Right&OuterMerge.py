import numpy as np
import pandas as pd

registrations = pd.DataFrame({'reg_id': [1, 2, 3, 4], 'name': ['Andrew', 'Bobo', 'Claire', 'David']})
logins = pd.DataFrame({'log_id': [1, 2, 3, 4], 'name': ['Xavier', 'Andrew', 'Yolanda', 'Bobo']})

f = pd.merge(left=registrations, right=logins, how='left', on='name')
print(f)
# order of passing left and right matters
# how = 'left' will give all the info in left table in the ans

t = pd.merge(left=logins, right=registrations, how='left', on='name')
print(t)

v = pd.merge(logins, registrations, how='outer', on='name')

# order of passing not matters as same as inner
print(v)

#  merge on index
registrations = registrations.set_index('name')

h = pd.merge(registrations, logins, left_index=True, right_on='name', how='inner')
# merge on registrations index and logins name column
print(h)
pd.merge(logins, registrations, right_index=True, left_on='name')
registrations = registrations.reset_index()
registrations.columns = ['reg_name', 'reg_id']
pd.merge(registrations, logins, left_on='reg_name', right_on='name')
pd.merge(registrations, logins, left_on='reg_name', right_on='name').drop('reg_name', axis=1)

# Pandas automatically tags duplicate columns
registrations.columns = ['name', 'id']

logins.columns = ['id', 'name']
pd.merge(registrations, logins, on='name')
pd.merge(registrations, logins, on='name', suffixes=('_reg', '_log'))
