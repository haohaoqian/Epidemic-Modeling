import json
import numpy as np
import matplotlib.pyplot as plt

with open('D:\\郝千越文件\\其他\\SRT\\RL疫情控制\\data\\result_500days.json','r') as f:
    data=np.array(json.load(f))

plt.plot(range(len(data)),np.sum(data[:,:,1],axis=1),label='L')
plt.plot(range(len(data)),np.sum(data[:,:,2],axis=1),label='I')
plt.plot(range(len(data)),np.sum(data[:,:,3],axis=1),label='Ia')
plt.plot(range(len(data)),np.sum(data[:,:,4],axis=1),label='Ih')
#plt.plot(range(len(data)),np.sum(data[:,:,5],axis=1),label='R')
#plt.plot(range(len(data)),np.sum(data[:,:,6],axis=1),label='D')
plt.legend()
plt.show()

'''
I=list()
I.append(sum(data[0,:,2]))
for i in range(1,2880):
    I.append(sum(data[i,:,2])+sum(data[i,:,3])+sum(data[i,:,4])+sum(data[i,:,5])+sum(data[i,:,6]))
plt.plot(range(2880),I,label='predict')
plt.plot([0,48,96,144,192,240,288,336,384,432],[1,7,43,79,108,139,150,175,200,222],label='ground truth')
plt.legend()
plt.show()
'''