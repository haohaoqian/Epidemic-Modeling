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
data2=np.zeros((365,675))
for i in range(675):
    for j in range(365):
        if(np.sum(data[j*48][i])!=0):
            data2[j][i]=(np.sum(data[j*48][i])-data[j*48][i][0]-data[j*48][i][-1]-data[j*48][i][-2])/np.sum(data[j*48][i])
        else:
            data2[j][i]=0
for j in range(365):
    tempx=[]
    tempy=[]
    tempc=[]
    for i in range(675):
        tempx.append(flow[i])
        tempy.append(dense[i])
        tempc.append(data2[j][i])
    plt.figure(figsize=(20,15))
    plt.scatter(tempx,tempy,c=tempc,marker='.',cmap=cm.Reds,vmin=0,vmax=0.3)
    plt.colorbar()
    plt.grid()
    plt.xlabel('Relatively flow')
    plt.ylabel('Relatively population-density')
    plt.xlim(0.2,1.1)
    plt.ylim(-0.1,1.1)
    plt.title('Epidemic situation at {}days'.format(j+1))
    plt.savefig('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\{}.png'.format(j+1))