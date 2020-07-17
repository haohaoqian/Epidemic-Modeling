import json
import matplotlib.pyplot as plt
import numpy as np

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\dense_region.json','r') as f:
    dense=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\flow_region.json','r') as f:
    flow=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region_marker.json','r') as f:
    marker=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-acc-1.json','r') as f:
    para1=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-acc-2.json','r') as f:
    para2=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-acc-3.json','r') as f:
    para3=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-acc-4.json','r') as f:
    para4=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-acc-5.json','r') as f:
    para5=json.load(f)

marker=np.array(marker)
dense=np.array(dense)*marker
dense=dense[dense!=0]
flow=np.array(flow)*marker
flow=flow[flow!=0]

para1=np.array(para1)
para2=np.array(para2)
para3=np.array(para3)
para4=np.array(para4)
para5=np.array(para5)

t1=para1[:,2]
t2=para2[:,2]
t3=para3[:,2]
t4=para4[:,2]
t5=para5[:,2]
t1=t1*marker
t1=t1[t1!=0]
t2=t2*marker
t2=t2[t2!=0]
t3=t3*marker
t3=t3[t3!=0]
t4=t4*marker
t4=t4[t4!=0]
t5=t5*marker
t5=t5[t5!=0]
t=(t1+t2+t3+t4+t5)/5

fig=plt.figure(figsize=(20,15))
plt.scatter(dense,t,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0,np.max(dense)*1.05)
plt.xlabel('Population density(people/km^2)')
plt.ylabel('Para-t',fontsize=15)
plt.title('Population density & Para-t',fontsize=15)
plt.show()

fig=plt.figure(figsize=(20,15))
plt.scatter(flow,t,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0.2,1.05)
plt.xlabel('Relatively flow')
plt.ylabel('Para-t',fontsize=15)
plt.title('Relatively flow & Para-t',fontsize=15)
plt.show()

p=np.corrcoef([dense,flow,t])
print(p)

t1=para1[:,4]
t2=para2[:,4]
t3=para3[:,4]
t4=para4[:,4]
t5=para5[:,4]
t1=t1*marker
t1=t1[t1!=0]
t2=t2*marker
t2=t2[t2!=0]
t3=t3*marker
t3=t3[t3!=0]
t4=t4*marker
t4=t4[t4!=0]
t5=t5*marker
t5=t5[t5!=0]
t=(t1+t2+t3+t4+t5)/5
print(np.mean(t))