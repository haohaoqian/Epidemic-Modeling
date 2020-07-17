import json
import numpy as np

LIST=[0.5,0.1,0.05,0.01,0.005,0.001,0.0005,0.0001]
for x in LIST:
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment8\\result-500d-{}traffic.json'.format(x),'r') as f:
        data=np.array(json.load(f))

    s=list()
    for i in range(365*48):
        s.append([np.sum(data[i][:,0]),np.sum(data[i][:,1]),np.sum(data[i][:,2]),np.sum(data[i][:,3]),np.sum(data[i][:,4]),np.sum(data[i][:,5]),np.sum(data[i][:,6])])
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment8\\result-365d-{}traffic-sum.json'.format(x),'w') as f:
        json.dump(s,f)