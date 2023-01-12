import pandas as pd
import numpy as np


df = pd.read_excel('BugSet2.xlsx', engine='openpyxl')
print(df)
print(type(df))
root_cause = df['Root_Causes'].to_list()
symptoms=df['Symptoms'].to_list()
df['Opened']=pd.to_datetime(df['Opened'])
df['Closed']=pd.to_datetime(df['Closed'])
leadtime3=(df['Closed'] - df['Opened']).map(lambda x:x.days)
df['Duration_Date']=leadtime3


for (k1, k2), group in df.groupby(['Root_Causes', 'Symptoms']):
	print(type((k1, k2)),(k1, k2),len(group),type(group))
	print(group)

