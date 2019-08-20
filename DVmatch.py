import pandas as pd
from pandas import DataFrame, read_excel, merge, ExcelWriter

#matches against OCLC numbers
df_1 = read_excel('U:\\...WL-UTL data.xlsx', sheet_name='WL-OCLC')
df_2 = read_excel('U:\\...WL-UTL data.xlsx', sheet_name='UTL-OCLC')
df_3 = df_1.merge(df_2, on='OCLC', how='inner')
df_4 = read_excel('U:\\...WL-UTL data.xlsx', sheet_name='WL-ISBN')
df_5 = read_excel('U:\\...WL-UTL data.xlsx', sheet_name='UTL-ISBN')
df_6 = df_4.merge(df_5, on='ISBN', how='inner')
df_7 = df_3.merge(df_6, how='outer')
df_8 =df_4.merge(df_7, how='left')

# writes a new spreadsheet
writer = pd.ExcelWriter('U:\\...WL-UTL match.xlsx', engine='xlsxwriter')
df_3.to_excel(writer, sheet_name='OCLC')
df_6.to_excel(writer, sheet_name='ISBN')
df_7.to_excel(writer, sheet_name='COMBINED')
df_8.to_excel(writer, sheet_name='UNMATCHED')
writer.save()
