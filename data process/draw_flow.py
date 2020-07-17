import json
import numpy as np
import matplotlib.pyplot as plt

region_beijing = json.load(open("D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\raw\\region_beijing_tencent.json"))
center_downtown = region_beijing["center"]
downtown_beijing = region_beijing["boundary"]
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\od_prob.json','r') as f:
    od=np.array(json.load(f))

od228=od[16]*800

plt.figure(figsize=(6.4,4.76))
cl=['limegreen','lime','lawngreen','greenyellow','yellow','gold','orange','darkorange','orangered','red']
for i in range(len(downtown_beijing)):
    tmp = np.array(downtown_beijing[i])
    plt.plot(tmp[:,0],tmp[:,1],color='black',linewidth=0.5)
for i in range(250,350):
    for j in range(675):
        if(i!=j):
            if(od228[i][j]>=0.9):
                od228[i][j]=0.9
            if(od228[i][j]>0):
                plt.plot([center_downtown[i][0],center_downtown[j][0]],[center_downtown[i][1],center_downtown[j][1]],color=cl[int(10*od228[i][j])],linewidth=0.5,alpha=0.5)
plt.tick_params(labelsize=15)
plt.xlabel('East-longitude($\\degree$)',fontsize=20)
plt.ylabel('North-latitude($\\degree$)',fontsize=20)
plt.subplots_adjust(left=0.2,bottom=0.2)

plt.savefig('c:\\users\\郝千越\\desktop\\strength1.png',dpi=100)