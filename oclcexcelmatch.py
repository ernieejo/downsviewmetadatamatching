import pandas as pd
from pandas import DataFrame, read_excel, merge

#matches against OCLC numbers
df_1 = read_excel('filepath to [YOUR LIBRARY]1.xlsx')
df_2 = read_excel('filepath to utl1.xlsx')
df_3 = df_1.merge(df_2, on='OCLC', how='left')
df_3.to_excel('filepath to write oclcmatches.xlsx')
