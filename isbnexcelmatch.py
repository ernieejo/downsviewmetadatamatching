import pandas as pd
from pandas import DataFrame, read_excel, merge

#matches against ISBN numbers
df_1 = read_excel('filepath to wl2.xlsx')
df_2 = read_excel('filepath to utl2.xlsx')
df_3 = df_1.merge(df_2, on='ISBN', how='left')
df_3.to_excel('filepath to write isbnmatches.xlsx')
