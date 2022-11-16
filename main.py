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

# print(df.shape)
# print(df.columns)

# Sorting data by investigation type 
sorting = df.sort_values("INVEST")

# Limit data to only criminal investigations, remove unused columns 
investigation_type = df['INVEST'].value_counts()["CRIM"]
# print(investigation_type)  #count 446
df = df.iloc[:446, :16]
# print(df.INVEST.head)

# Calculate the number of NANs in the columns
count_nan_fggopen = df['FGGOPEN'].isna().sum()
# print(count_nan_fggopen) # count = 239
count_nan_open = df['OPEN'].isna().sum()
# print(count_nan_open) # count = 11
count_nan_clear = df['CLEAR'].isna().sum()
# print(count_nan_clear) # count = 0 

# Remove NANs
df = df.dropna(subset=['OPEN'])

# Remove line with nonesense data
# print(df.iloc[343, 13])
df = df.drop(index=354 , axis=0)
# print(df.OPEN[330:350])

# print(df[df['OPEN'].isna()])
# print(df[df['FGGOPEN'].isna()])

# Convert to datetime, remove everything but year
def date_convert(date_to_convert):
     return datetime.datetime.strptime(date_to_convert, '%m%d%Y').strftime("%Y-%m-%d")

df['open_year'] = pd.DatetimeIndex(df['OPEN']).year
# print(df.open_year.head)
df['clear_year'] = pd.DatetimeIndex(df['CLEAR']).year
# print(df.clear_year.head)
df['fggopen_year'] = pd.DatetimeIndex(df['FGGOPEN']).year
# print(df.fggopen_year.head)


# Convert years into initgers 


# print(df.FGGOPEN.dtype)
# print(df.groupby("FGGOPEN").mean())

# print(df.OPEN.head)
# print(df.FGGOPEN.head)
# print(df.CLEAR.head)

# subtract open date from clear date; subtract clear date from FGG date