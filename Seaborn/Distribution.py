

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv('dm_office_sales.csv')

a = df.head()

print(a)

# plt.figure(fig-size=(9,9) , dpi= 100)
sns.rugplot(x='salary', data=df, height=0.5)

# do not use DIST PLOT  # depreciated
# sns.dis plot
# sns.his plot

sns.set(style='darkgrid')
sns.displot(data=df, x='salary', bins=100, color='red', edgecolor='blue', linewidth=1, ls='--', kde=True, rug=True)

sns.histplot(data=df, x='salary')

sns.kdeplot(data=df, x='salary')

np.random.seed(42)
sampleages = np.random.randint(0, 100, 200)
print(sampleages)

sampleages = pd.DataFrame(sampleages, columns=['age'])
print(sampleages)

sns.rugplot(data=sampleages, x='age')

sns.histplot(data=sampleages, x='age')

sns.displot(data=sampleages, x='age', rug=True, bins=30, kde=True)

sns.kdeplot(data=sampleages, x='age', clip=[0, 100], bw_adjust=0.1, shade=True)
