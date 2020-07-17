import json
import numpy as np

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\od_prob.json','r') as f:
    data=json.load(f)
data=np.array(data)
data=np.sum(data,axis=0)
flow=np.zeros(675)
for i in range(675):
    flow[i]=np.sum(data[:,i])+np.sum(data[i,:])
    print('{}/675'.format(i+1))
m=np.max(flow)
flow=flow/m
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\flow_region.json','w') as f:
    json.dump(flow.tolist(),f)