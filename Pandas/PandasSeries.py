import numpy as np
import pandas as pd

# print(help(pd.Series))

myIndex = ['USA', 'Canada', 'mexico']
myData = [1776, 1867, 1821]
mySer = pd.Series(data=myData, index=myIndex)  # pandas series
print(mySer)

print(mySer[0])  # numeric index by location

print(mySer['USA'])  # labeled Index

ages = {'Sam': 5, 'Frank': 10, 'Spike': 7}
a = pd.Series(ages)  # keys as data  & values as indexes
print(a)

Q1 = {'japan': 80, 'China': 450, 'India': 200, 'USA': 500}
Q2 = {'Brazil': 100, 'China': 500, 'India': 210, 'USA': 260}
sales_q1 = pd.Series(Q1)
sales_q2 = pd.Series(Q2)

print(sales_q1['japan'])

print(sales_q1.keys())

print(sales_q1 * 2)  # broadcasting work since pandas series is a numpy array

print(sales_q1 + sales_q2)  # not present will default give Nan

print(sales_q1.add(sales_q2, fill_value=0))  # to have a default no if not present in any series

# after performing operations majorly give float numbers in ans
