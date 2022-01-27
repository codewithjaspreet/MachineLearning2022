import pandas as pd
import numpy as np

df = pd.read_csv('tips.csv')
print(df.head())


def last_four(num):
    return int(str(num)[-4:])


print(last_four(123456789))
# .apply() method
# for a method to be used in apply method it should return a single value
df['last_four'] = df['CC Number'].apply(last_four)
print(df.head())


def simple(num):
    return num * 2


print(simple(2))

print(lambda num: num * 2)

print(df['CC Number'].apply(lambda emp: emp * 2))


def quality(total_bill, tip):
    if tip / total_bill > 0.25:
        return "Generous"
    else:
        return "Other"


print(df[['total_bill', 'tip']].apply(lambda df: quality(df['total_bill'], df['tip']), axis=1))

# np.vectorize : faster

df['Quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])
print(df.head())
# np.vectorize makes function numpy aware,
# and it is faster than lambda
