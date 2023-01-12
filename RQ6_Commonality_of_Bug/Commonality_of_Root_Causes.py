import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('font',family='Times New Roman')

df = pd.DataFrame({
  'SpiderMonkey': [62, 72, 26, 19, 28, 17, 22, 6, 7, 22, 5, 11, 14, 3, 6, 5],
  'Wasmer': [45, 33, 44, 17, 10, 16, 0, 2, 27, 2, 13, 7, 0, 4, 2, 2],
  'V8': [66, 36, 17, 14, 9, 6, 23, 28, 1, 8, 4, 0, 1, 4, 1, 2],
  'WasmTime': [48, 7, 8, 5, 4, 7, 1, 1, 2, 5, 4, 3, 0, 1, 2, 0]})

corr = df.corr('spearman')

x = np.array([[False, True, True, True],
              [False, False, True, True],
              [False, False, False, True],
              [False, False, False, False]])
f, ax = plt.subplots(figsize=(10,8))

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
sns.heatmap(corr, center=0, annot=True, cmap='YlGnBu',mask=x, annot_kws={"size":18},cbar=False)
plt.savefig('Correlation_of_Root_Causes.png')
plt.show()