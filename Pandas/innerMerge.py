import numpy as np
import pandas as pd

registrations = pd.DataFrame({'reg_id': [1, 2, 3, 4], 'name': ['Andrew', 'Bobo', 'Claire', 'David']})
logins = pd.DataFrame({'log_id': [1, 2, 3, 4], 'name': ['Xavier', 'Andrew', 'Yolanda', 'Bobo']})

print(registrations)
print(logins)
f = pd.merge(registrations, logins, how='inner', on='name')
# inner return the keys & their respective values which are present in both tables
# passing order columns  not matters
print(help(pd.merge))
print(f)
