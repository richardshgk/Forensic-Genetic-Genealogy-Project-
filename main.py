# bring in modules (matplotlib, pandas)
import matplotlib.pyplot as plt
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
df = df.dropna(subset=['FGGOPEN'])
# print(df.shape)

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


# Find number of years to close case from open, number of years to close case after sending for FGG
df["open_to_close"] = df['clear_year'] - df['open_year']
# print(df['open_to_close'].head)
df["fggopen_to_close"] = df['clear_year'] - df['fggopen_year']
# print(df['fggopen_to_close'].head)


# open_count = df["open_to_close"].value_counts(sort=False)
# fggopen_count = df["fggopen_to_close"].value_counts(ascending=True)
# print(open_count)
# print(fggopen_count)


# Create and format histogram 
plt.style.use("ggplot")
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Closing Cases Using Forensic Genetic Geneology(FGG)')
# ax1.plot(x, y)
# ax2.plot(x, -y)

bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

plt.hist(df['open_to_close'], bins=bins, edgecolor="black", alpha=0.5, label="Total")
plt.hist(df['fggopen_to_close'], bins=bins, edgecolor="black", alpha=0.5, label="After FGG Initiated")

plt.title("")
plt.xlabel("Years")
plt.ylabel("Number of Cases")
plt.legend()

plt.show()

