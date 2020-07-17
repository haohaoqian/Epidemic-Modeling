import json
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import numpy as np


with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\dense_region.json','r') as f:
    Dense=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\flow_region.json','r') as f:
    Flow=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\peak_record.json','r') as f:
    data=json.load(f)

LIST=[670,607,236,587,411,28,124,505,498,501,387,666]
dense=[]
flow=[]
data=np.array(data)
height=data[:,0]
var_height=np.std(height)/np.mean(height)
print(var_height)
date=data[:,1]
var_date=np.std(date)/np.mean(date)
print(var_date)
for i in LIST:
    dense.append(Dense[i])
    flow.append(Flow[i])
date=date/48
fig=plt.figure(figsize=(20,15))
plt.scatter(dense,height,marker='o')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Population density(people/km^2)',fontsize=15)
plt.ylabel('Peak-height',fontsize=15)
plt.title('Start region-Population density & Peak-height',fontsize=15)
plt.ylim(0.15,0.25)
plt.show()
fig=plt.figure(figsize=(20,15))
plt.scatter(dense,date,marker='o')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Population density(people/km^2)',fontsize=15)
plt.ylabel('Peak-date',fontsize=15)
plt.title('Start region-Population density & Peak-date',fontsize=15)
plt.ylim(130,160)
plt.show()
fig=plt.figure(figsize=(20,15))
plt.scatter(flow,height,marker='o')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Relatively flow',fontsize=15)
plt.ylabel('Peak-height',fontsize=15)
plt.title('Start region-Relatively flow & Peak-height',fontsize=15)
plt.ylim()
plt.ylim(0.15,0.25)
plt.show()
fig=plt.figure(figsize=(20,15))
plt.scatter(flow,date,marker='o')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Relatively flow',fontsize=15)
plt.ylabel('Peak-date',fontsize=15)
plt.title('Start region-Relatively flow & Peak-date',fontsize=15)
plt.ylim(130,160)
plt.show()