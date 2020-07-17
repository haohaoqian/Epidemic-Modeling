import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\dense_region.json','r') as f:
    dense=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\flow_region.json','r') as f:
    flow=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\marker_region.json','r') as f:
    marker=json.load(f)

LIST=[670,607,236,587,411,28,124,505,498,501,387,666,101]

flow=np.array(flow)
dense=np.array(dense)
marker=np.array(marker)

flow=flow*marker
dense=dense*marker

fmax=np.max(flow)
dmax=np.max(dense)

plt.figure(figsize=(6.4,4.76))
for i in LIST:
    if(marker[i]==1):
        plt.scatter(flow[i]/fmax,dense[i]/dmax,marker='o',color='blue')
plt.xlabel('Relative population flow',fontsize=23)
plt.ylabel('Relative population density',fontsize=23)
plt.xlim(0.3,1)
plt.tick_params(labelsize=20)
plt.subplots_adjust(left=0.2,bottom=0.2)
plt.savefig('c:\\users\\郝千越\\desktop\\feature2.png',dpi=100)