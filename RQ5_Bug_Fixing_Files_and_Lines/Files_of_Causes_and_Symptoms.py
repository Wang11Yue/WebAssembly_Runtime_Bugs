import pandas as pd
import numpy as np


df = pd.read_excel('BugSet3.xlsx', engine='openpyxl')
print(df)
print(type(df))
root_cause = df['Root_Causes'].to_list()
symptoms=df['Symptoms'].to_list()

for K1, group in df.groupby(['Root_Causes']):
    print('#files: ')
    print(K1)
    print('mean: ', group['#files'].mean())
    print('median: ', group['#files'].median())
    print('std: ', group['#files'].std())
    print('min: ', group['#files'].min())
    print('max: ', group['#files'].max())
    print('---------------------------------')


