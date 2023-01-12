import pandas as pd
import numpy as np


df = pd.read_excel('BugSet3.xlsx', engine='openpyxl')
print(df)
print(type(df))
root_cause = df['root cause'].to_list()
symptoms=df['symptoms1'].to_list()
df['Opened']=pd.to_datetime(df['Opened'])
df['Closed']=pd.to_datetime(df['Closed'])
leadtime3=(df['Closed'] - df['Opened']).map(lambda x:x.days)
df['Duration_Date']=leadtime3


for K1, group in df.groupby(['root cause']):
	print('#lines: ')
	print(K1)
	print('mean: ', group['#lines'].mean())
	print('median: ', group['#lines'].median())
	print('std: ', group['#lines'].std())
	print('min: ', group['#lines'].min())
	print('max: ', group['#lines'].max())


