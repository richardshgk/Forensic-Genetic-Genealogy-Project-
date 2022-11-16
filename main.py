# bring in modules (matplotlib, pandas)
import matplotlib as plt
import pandas as pd
import numpy as np
import datetime

# read in excel file
df = pd.read_excel(r'assets\FGG_Database_v_2021_3.xlsx')

# Replace null values and remove last line from dataframe 
df.replace('nd', np.nan, inplace=True)
df = df.iloc[:-1 , :]

# (data came presorted by investigation type)

# Limiting data to only criminal investigations 
# investigation_type = df['INVEST'].value_counts()["CRIM"]
# print(investigation_type)  #count 446
df = df.iloc[:446, :]

# print(df.INVEST.head)

#print(df.shape)
#print(df.columns)

def date_convert(date_to_convert):
     return datetime.datetime.strptime(date_to_convert, '%m%d%Y').strftime("%Y-%m-%d")

open = df.OPEN
FGG_open = df.FGGOPEN
closed = df.CLEAR

df['open_year'] = pd.DatetimeIndex(df['OPEN']).year
print(df.open_year.head)

# print(df.OPEN.head)
# print(df.FGGOPEN.head)
# print(df.CLEAR.head)

# reformat all dates to match each other. find out how many FGG start dates are empty and decide how to proceed from there. 

# subtract open date from FGG date; subtract close date from FGG date