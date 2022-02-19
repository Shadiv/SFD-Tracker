# Imports

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

# Training url
url_1 = "https://www.sec.gov/Archives/edgar/data/0001274494/000127449421000030/aex991pressreleaseq3x2021.htm"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36'}
r1 = requests.get(url_1, headers=headers)
r_clean = r1.text
soup = BeautifulSoup(r_clean, "html.parser")
df = pd.read_html(r_clean)
tab1 = df[2]
tab1 = tab1.dropna(axis=1, how='all')
pd.set_option('display.max_columns', None)
# pd set option to display all the columns and rows.

tab1.columns = [i for i in range(len(tab1.columns))]
# rename columns, so index = col_name

copies = {}
#there is a lot of similar data inside the table (almost duplicite columns. Parcing doesn't work well enough).
# That is why we need to get rid of them
for i in tab1:
    dups = []
    for n in range(len(tab1.columns)):
        if np.sum(np.where(tab1[i] == tab1[n], True, False)) > 3 and i != n:
            dups.append(n)
    # uses loop to identifie duplicate data between two columns, and if there is more than 3 dups (table still includes some NaN cells, so it cannot be without dups), it appends duplicate column to "dups".
    copies[i] = [*dups]
    #every column in compared with every other column
unique_cols = [i for i in range(len(tab1.columns)) if len(copies[i]) < 2 and copies[i] != []]
#list of unique columns
indexes = [i for i in tab1[0]]
#indexes = names of items inside balance sheet.
for i in range(len(tab1.columns)): # cleaning.
    if i not in unique_cols:
        del tab1[i]

col_names = [tab1[i][1] for i in tab1] # setting column names to period end (End of quater - 30th sept, dec, etc)
tab1.columns = [i for i in col_names]
tab1.index = indexes #setting row indexes to balance sheet items
tab1 = tab1[:][2:] # get rid of NaN on top
tab1 = tab1.replace(np.nan, '') #replacing nan with empty string
tab1.replace()
values = tab1.loc['Cash and cash equivalents']