import json
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\dense_region.json','r') as f:
    dense=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\flow_region.json','r') as f:
    flow=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region_marker.json','r') as f:
    marker=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\start-result-365d-average-1.json','r') as f:
    start1=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\start-result-365d-average-2.json','r') as f:
    start2=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\start-result-365d-average-3.json','r') as f:
    start3=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\start-result-365d-average-4.json','r') as f:
    start4=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\start-result-365d-average-5.json','r') as f:
    start5=json.load(f)

marker=np.array(marker)
dense=np.array(dense)-10000000*marker
flow=np.array(flow)-10000000*marker
start1=np.array(start1)
start2=np.array(start2)
start3=np.array(start3)
start4=np.array(start4)
start5=np.array(start5)

fig=plt.figure(figsize=(20,15))
plt.scatter(dense,start1,marker='o',color='red')
plt.scatter(dense,start2,marker='o',color='red')
plt.scatter(dense,start3,marker='o',color='red')
plt.scatter(dense,start4,marker='o',color='red')
plt.scatter(dense,start5,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0,np.max(dense)*1.05)
plt.ylim(-0.5,22)
plt.xlabel('Population density(people/km^2)')
plt.ylabel('Start-date(day)',fontsize=15)
plt.title('Population density & Start-date',fontsize=15)
plt.show()

fig=plt.figure(figsize=(20,15))
plt.scatter(flow,start1,marker='o',color='red')
plt.scatter(flow,start2,marker='o',color='red')
plt.scatter(flow,start3,marker='o',color='red')
plt.scatter(flow,start4,marker='o',color='red')
plt.scatter(flow,start5,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0.2,1.1)
plt.ylim(-0.5,22)
plt.xlabel('Relatively flow',fontsize=15)
plt.ylabel('Start-date(day)',fontsize=15)
plt.title('Relatively flow & Start-date',fontsize=15)
plt.show()