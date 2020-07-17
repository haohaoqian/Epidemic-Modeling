import json
import numpy as np
import matplotlib.pyplot as plt

region_beijing = json.load(open("D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\raw\\region_beijing_tencent.json"))
center_downtown = region_beijing["center"]
downtown_beijing = region_beijing["boundary"]
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\marker_region.json','r') as f:
    marker=json.load(f)

plt.figure(figsize=(6.4,4.76))

for i in range(208,209):
	tmp = np.array(downtown_beijing[i])
	plt.plot(tmp[:,0],tmp[:,1],linewidth=1)
'''
	if(marker[i]):
		plt.fill(tmp[:,0],tmp[:,1],facecolor='red')
'''
tmp = np.array(downtown_beijing[170])
plt.plot(tmp[:,0],tmp[:,1],linewidth=1)
tmp = np.array(downtown_beijing[168])
plt.plot(tmp[:,0],tmp[:,1],linewidth=1)
tmp = np.array(downtown_beijing[169])
plt.plot(tmp[:,0],tmp[:,1],linewidth=1)
tmp = np.array(downtown_beijing[205])
plt.plot(tmp[:,0],tmp[:,1],linewidth=1)
tmp = np.array(downtown_beijing[231])
plt.plot(tmp[:,0],tmp[:,1],linewidth=1)
plt.plot(116.332769,39.8119335,marker='*')
plt.tick_params(labelsize=15)
plt.xlabel('East-longitude($\\degree$)',fontsize=20)
plt.ylabel('North-latitude($\\degree$)',fontsize=20)
plt.subplots_adjust(left=0.2,bottom=0.2)
plt.show()
#plt.savefig('c:\\users\\郝千越\\desktop\\blocks.png',dpi=100)
