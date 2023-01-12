import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator
import scipy.stats as stats
plt.rc('font',family='Times New Roman')
print('---------------------------------spidermonkey---------------------------------------')
df_spidermonkey=pd.read_excel('BugSet3_SpiderMonkey.xlsx', engine='openpyxl')
sm_line_um_list=df_spidermonkey['#Lines'].values.tolist()
print('#Lines:   ')
print('mean: ',df_spidermonkey['#Lines'].mean())
print('median: ',df_spidermonkey['#Lines'].median())
print('std: ',df_spidermonkey['#Lines'].std())
print('max: ',df_spidermonkey['#Lines'].max())
print('min: ',df_spidermonkey['#Lines'].min())


print('---------------------------------v8---------------------------------------')
df_v8=pd.read_excel('BugSet3_V8.xlsx', engine='openpyxl')
v8_line_um_list=df_v8['#Lines'].values.tolist()
print('#Lines:   ')
print('mean: ',df_v8['#Lines'].mean())
print('median: ',df_v8['#Lines'].median())
print('std: ',df_v8['#Lines'].std())
print('max: ',df_v8['#Lines'].max())
print('min: ',df_v8['#Lines'].min())

print('---------------------------------wasmer---------------------------------------')
df_wasmer=pd.read_excel('BugSet3_Wasmer.xlsx', engine='openpyxl')
ws_line_um_list=df_wasmer['#Lines'].values.tolist()
print('#Lines:   ')
print('mean: ',df_wasmer['#Lines'].mean())
print('median: ',df_wasmer['#Lines'].median())
print('std: ',df_wasmer['#Lines'].std())
print('max: ',df_wasmer['#Lines'].max())
print('min: ',df_wasmer['#Lines'].min())

print('---------------------------------wasmtime---------------------------------------')
df_wasmtime=pd.read_excel('BugSet3_Wasmtime.xlsx', engine='openpyxl')
wt_line_um_list=df_wasmtime['#Lines'].values.tolist()
print('#Lines:   ')
print('mean: ',df_wasmtime['#Lines'].mean())
print('median: ',df_wasmtime['#Lines'].median())
print('std: ',df_wasmtime['#Lines'].std())
print('max: ',df_wasmtime['#Lines'].max())
print('min: ',df_wasmtime['#Lines'].min())

print('------------------------draw picture!------------------------')
#,defaultreallimits=(1,1000) 从小于1开始算个数
res_sm=stats.cumfreq(sm_line_um_list, numbins=1000,defaultreallimits=(1,1000))
res_v8=stats.cumfreq(v8_line_um_list, numbins=1000,defaultreallimits=(1,1000))
res_ws=stats.cumfreq(ws_line_um_list, numbins=1000,defaultreallimits=(1,1000))
res_wt=stats.cumfreq(wt_line_um_list, numbins=1000,defaultreallimits=(1,1000))
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

ax.set_ylim(0, 1.01)
ax.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])
plt.yticks(fontsize=14)
plt.xticks([1,36,110,200,301,348,500,600,700,800,900,1000],rotation=360,fontsize=14)
plt.plot(x1,res_sm[0] / 325, label="SpiderMonkey",color='b') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
plt.plot(x2,res_v8[0] / 196, label="V8",color ='r') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
plt.plot(x3,res_ws[0] / 209, label="Wasmer",color='c') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
plt.plot(x4,res_wt[0] / 88, label="Wasmtime",color ='m') #把每个柱形的高度的中间点连起来Vplt.xlabel("X")
#---print(res_sm[0][99] / 325)  #真正的坐标【0，1000】，定义的坐标【1，1000】
#plt.text(100, res_sm[0][99]/325, '(100, 90%)', fontsize=10, style ="italic", weight ="light", verticalalignment='center', horizontalalignment='left')
print(res_sm[0][109]/325)
print(res_v8[0][109]/196)
print(res_ws[0][300]/209)
print(res_wt[0][347]/88)
print(res_wt[0][35]/88)
plt.xlabel("Number of lines of code in a Fix",fontsize=16,labelpad = 6)
plt.ylabel("Fraction of Bugs",fontsize=16,labelpad = 6)

plt.legend(loc='lower right',fontsize=16)
#plt.xticks([1,100,200,300,400,500,800])
#plt.yticks([0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0])
# 添加网格线
plt.grid(linestyle="--", alpha=0.5)
plt.savefig('Number_of_lines_of_code_in_a_Fix.png')
print(plt.show())


plt.figure(figsize=(10,8))
