# bring in modules (matplotlib, pandas)
import matplotlib as plt
import pandas as pd
import numpy as np

# read in excel file
df = pd.read_excel(r'assets\FGG_Database_v_2021_3.xlsx')

df.replace('00', '01', inplace=True)
df.replace('nd', np.nan, inplace=True)

#print(df.shape)
#print(df.columns)

open = df.OPEN
FGG_open = df.FGGOPEN
closed = df.CLEAR
pd.to_datetime(df['OPEN'])
print(df.OPEN.dtype) #object
print(df.FGGOPEN.dtype) #object
print(df.CLEAR.dtype) #object

# find column names of type of investigation, open date, close date, FGG start date
#print(df.columns)

# reformat all dates to match each other. find out how many FGG start dates are empty and decide how to proceed from there. 

# subtract open date from FGG date; subtract close date from FGG date