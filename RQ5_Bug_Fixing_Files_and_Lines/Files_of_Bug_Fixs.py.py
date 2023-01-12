import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator
import scipy.stats as stats
plt.rc('font',family='Times New Roman')
print('---------------------------------spidermonkey---------------------------------------')
df_spidermonkey=pd.read_excel('BugSet3_SpiderMonkey.xlsx', engine='openpyxl')
sm_file_um_list=df_spidermonkey['#Files'].values.tolist()

print('#Files: ')
print('mean: ', df_spidermonkey['#Files'].mean())
print('median: ', df_spidermonkey['#Files'].median())
print('std: ', df_spidermonkey['#Files'].std())
print('max: ',df_spidermonkey['#Files'].max())
print('min: ',df_spidermonkey['#Files'].min())


print('---------------------------------v8---------------------------------------')
df_v8=pd.read_excel('BugSet3_V8.xlsx', engine='openpyxl')
v8_file_um_list=df_v8['#Files'].values.tolist()

print('#Files: ')
print('mean: ', df_v8['#Files'].mean())
print('median: ', df_v8['#Files'].median())
print('std: ', df_v8['#Files'].std())
print('max: ',df_v8['#Files'].max())
print('min: ',df_v8['#Files'].min())

print('---------------------------------wasmer---------------------------------------')
df_wasmer=pd.read_excel('BugSet3_Wasmer.xlsx', engine='openpyxl')
ws_file_um_list=df_wasmer['#Files'].values.tolist()

print('#Files: ')
print('mean: ', df_wasmer['#Files'].mean())
print('median: ', df_wasmer['#Files'].median())
print('std: ', df_wasmer['#Files'].std())
print('max: ',df_wasmer['#Files'].max())
print('min: ',df_wasmer['#Files'].min())

print('---------------------------------wasmtime---------------------------------------')
df_wasmtime=pd.read_excel('BugSet3_Wasmtime.xlsx', engine='openpyxl')
wt_file_um_list=df_wasmtime['#Files'].values.tolist()

print('#Files: ')
print('mean: ', df_wasmtime['#Files'].mean())
print('median: ', df_wasmtime['#Files'].median())
print('std: ', df_wasmtime['#Files'].std())
print('max: ',df_wasmtime['#Files'].max())
print('min: ',df_wasmtime['#Files'].min())

print('------------------------draw picture!------------------------')
#,defaultreallimits=(1,1000) 从小于1开始算个数
res_sm=stats.cumfreq(sm_file_um_list, numbins=50, defaultreallimits=(1, 50))
res_v8=stats.cumfreq(v8_file_um_list, numbins=50, defaultreallimits=(1, 50))
res_ws=stats.cumfreq(ws_file_um_list, numbins=50, defaultreallimits=(1, 50))
res_wt=stats.cumfreq(wt_file_um_list, numbins=50, defaultreallimits=(1, 50))
print(res_wt[0])
print(type(res_sm[0]))
print('第一个柱形中心起始点')
print(res_v8.lowerlimit)
lowerlimit_sm=res_sm.lowerlimit
lowerlimit_v8=res_v8.lowerlimit
lowerlimit_ws=res_ws.lowerlimit
lowerlimit_wt=res_wt.lowerlimit
lowerlimit=(lowerlimit_wt+lowerlimit_ws+lowerlimit_v8+lowerlimit_sm)/4
#柱形的宽度
print('柱形的宽度')
print(res_sm.binsize)
binsize_sm=res_sm.binsize
binsize_v8=res_v8.binsize
binsize_ws=res_ws.binsize
binsize_wt=res_wt.binsize
binsize=(binsize_sm+binsize_v8+binsize_ws+binsize_wt)/4
print(binsize)
#柱形的高度(x中的数值有多少个会积累落入该柱形中,元素的个数)
#print(res.cumcount)
print('柱形的高度(x中的数值有多少个会积累落入该柱形中,元素的个数)')
cumcount_sm=res_sm.cumcount #其实就是res_sm[0]
cumcount_v8=res_v8.cumcount
cumcount_ws=res_ws.cumcount
cumcount_wt=res_wt.cumcount
cumcount=(cumcount_wt+cumcount_ws+cumcount_sm+cumcount_v8)/4
x1= lowerlimit_sm + np.linspace(0, binsize_sm * cumcount_sm.size, cumcount_sm.size)
x2=lowerlimit_v8+np.linspace(0,binsize_v8*cumcount_v8.size,cumcount_v8.size)
x3=lowerlimit_ws+np.linspace(0,binsize_ws*cumcount_ws.size,cumcount_ws.size)
x4=lowerlimit_wt+np.linspace(0,binsize_wt*cumcount_wt.size,cumcount_wt.size)
x5=lowerlimit+np.linspace(0,binsize*cumcount.size,cumcount.size)

fig=plt.figure(figsize=(12, 8), dpi=100)
ax = fig.add_subplot(1,1,1)  #（xxx）这里前两个表示几*几的网格，最后一个表示第几子图

ax.set_ylim(0.4, 1.01)
ax.set_yticks([0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])

plt.xticks([1,4,6,8,10,14,20,30,40,50],fontsize=14)
plt.yticks(fontsize=14)
plt.plot(x1,res_sm[0] / 325, label="SpiderMonkey",color='b') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
plt.plot(x2,res_v8[0] / 196, label="V8",color ='r') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
plt.plot(x3,res_ws[0] / 209, label="Wasmer",color='c') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
plt.plot(x4,res_wt[0] / 88, label="Wasmtime",color ='m') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")

print(res_sm[0][0]/325)
print(res_v8[0][0]/196)
print(res_ws[0][13]/209)
print(res_wt[0][0]/88)

print(res_sm[0][3]/325)
print(res_v8[0][5]/196)
plt.xlabel("Number of files in a Fix",fontsize=16,labelpad = 6)
plt.ylabel("Fraction of Bugs",fontsize=16,labelpad = 6)

plt.legend(loc='lower right',fontsize=16)
#plt.xticks([1,100,200,300,400,500,800])
#plt.yticks([0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])
# 添加网格线
plt.grid(linestyle="--", alpha=0.5)
plt.savefig('Number_of_files_in_a_Fix.png')
print(plt.show())


plt.figure(figsize=(10,8))
