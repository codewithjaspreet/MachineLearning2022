import numpy as np
import pandas as pd

name = 'jaspreet@email.com'
print(name.split('@'))
print(name.isdigit())
names = pd.Series(['Jaspreet', 'Aryan', 'Claire', 'Ahip', 5])

print(names.str.upper())
print(names.str.isdigit())

# all python string methods can be applied

tech_finacne = ['Google,APPL,AMZN', 'JPN,BAC,GS']
tickers = pd.Series(tech_finacne)
print(tickers.str.split(','))
print(tickers.str.split(',', expand=True))  # expand true will give it in form of dataframe

messy_names = pd.Series(['andrew  ', "bo;bo", " claire "])
print(messy_names)
print(messy_names.str.replace(';', '').str.strip().str.capitalize())
