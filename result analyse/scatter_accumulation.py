import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\dense_region.json','r') as f:
    dense=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\flow_region.json','r') as f:
    flow=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment6\\result-365d-nonhospital-1.0traffic.json','r') as f:
    data=json.load(f)

dense=np.array(dense)
m=np.max(dense)
dense=dense/m
data=np.array(data)
data1=data[-1,:,:]
data2=[]
for i in range(675):
    if(np.sum(data1[i])!=0):
        data2.append((np.sum(data1[i])-data1[i][0])/np.sum(data1[i]))
    else:
        data2.append(0)
tempx=[]
tempy=[]
tempc=[]
for i in range(675):
    tempx.append(flow[i])
    tempy.append(dense[i])
    tempc.append(data2[i])
plt.figure(figsize=(20,15))
plt.scatter(tempx,tempy,c=tempc,marker='.',cmap=cm.Reds)
plt.colorbar()
plt.grid()
plt.xlabel('Relatively flow')
plt.ylabel('Relatively population')
plt.xlim(0.2,1.1)
plt.ylim(-0.1,1.1)
plt.title('Accumulated infected rate')
plt.savefig('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\acc.png')
plt.show()