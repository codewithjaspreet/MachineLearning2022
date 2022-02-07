import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dm_office_sales.csv')

a = df.head()

print(a)

plt.figure(figsize=(12, 4), dpi=200)
sns.scatterplot(x='salary', y='sales', data=df, alpha=0.2, hue='level of education', style='level of education')
plt.show()
plt.savefig('myplot.jpg')
