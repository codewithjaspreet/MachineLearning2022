import numpy as np
import pandas as pd
from datetime import datetime

myyear = 2015
myMonth = 1
myDay = 1
myHour = 2
myMin = 30
mySec = 15

myDate = datetime(myyear, myMonth, myDay)
print(myDate)
myDatetime = datetime(myyear, myMonth, myDay, myHour, myMin, mySec)
print(myDatetime)
myser = pd.Series(['Nov 3 , 1990', '2000-01-01', None])
print(myser)

# print(myser[0].year)

print(pd.to_datetime(myser))  # year - month -  date ->  default
timeSer = pd.to_datetime(myser)
print(timeSer[0].year)
euro = '31-12-2000'
print(pd.to_datetime(euro))
euro = '10-12-2000'
print(pd.to_datetime(euro, dayfirst=True))  # for date change

style_date = '12--Dec--2000'
print(pd.to_datetime(style_date, format='%d--%b--%Y'))
custom_date = "12th of Dec 2000"

print(pd.to_datetime(custom_date))

sales = pd.read_csv('RetailSales_BeerWineLiquor.csv')
sales['DATE'] = pd.to_datetime(sales['DATE'])
print(sales['DATE'][0].year)

sales = pd.read_csv('RetailSales_BeerWineLiquor.csv', parse_dates=[0])


sales = sales.set_index("DATE")

print(sales.resample(rule='A').mean())
print(sales['DATE'].dt.month)