import json
import matplotlib.pyplot as plt
import numpy as np

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment10\\分散\\result.json','r') as f:
    data=np.array(json.load(f))
region_beijing = json.load(open("D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\raw\\region_beijing_tencent.json"))
center_downtown = region_beijing["center"]
downtown_beijing = region_beijing["boundary"]

colormap=['white','yellow','orange','red','maroon']

for t in range(24,2880,24):
    plt.figure(figsize=(6.4,4.76))
    for i in range(675):
        tmp = np.array(downtown_beijing[i])
        plt.plot(tmp[:,0],tmp[:,1],linewidth=1)
        if(np.sum(data[t-24:t,i,2])+np.sum(data[t-24:t,i,4])+np.sum(data[t-24:t,i,6])<=20):
            n=0
        elif(np.sum(data[t-24:t,i,2])+np.sum(data[t-24:t,i,4])+np.sum(data[t-24:t,i,6])<=25):
            n=1
        elif(np.sum(data[t-24:t,i,2])+np.sum(data[t-24:t,i,4])+np.sum(data[t-24:t,i,6])<=30):
            n=2
        elif(np.sum(data[t-24:t,i,2])+np.sum(data[t-24:t,i,4])+np.sum(data[t-24:t,i,6])<=40):
            n=3
        else:
            n=4
        plt.fill(tmp[:,0],tmp[:,1],facecolor=colormap[n])
    plt.savefig('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment10\\fig\\{}.png'.format(t))