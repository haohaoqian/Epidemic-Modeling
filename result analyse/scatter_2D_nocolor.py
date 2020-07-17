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
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_date_region-1.json','r') as f:
    date1=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_height_region-1.json','r') as f:
    height1=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\acc_region-1.json','r') as f:
    acc1=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_date_region-2.json','r') as f:
    date2=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_height_region-2.json','r') as f:
    height2=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\acc_region-2.json','r') as f:
    acc2=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_date_region-3.json','r') as f:
    date3=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_height_region-3.json','r') as f:
    height3=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\acc_region-3.json','r') as f:
    acc3=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_date_region-4.json','r') as f:
    date4=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_height_region-4.json','r') as f:
    height4=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\acc_region-4.json','r') as f:
    acc4=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_date_region-5.json','r') as f:
    date5=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_height_region-5.json','r') as f:
    height5=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\acc_region-5.json','r') as f:
    acc5=json.load(f)

marker=np.array(marker)
dense=np.array(dense)*marker
dense=dense[dense!=0]
flow=np.array(flow)*marker
flow=flow[flow!=0]

date1=np.array(date1)*marker
date1=date1[date1!=0]
date2=np.array(date2)*marker
date2=date2[date2!=0]
date3=np.array(date3)*marker
date3=date3[date3!=0]
date4=np.array(date4)*marker
date4=date4[date4!=0]
date5=np.array(date5)*marker
date5=date5[date5!=0]
date1=date1/48
date2=date2/48
date3=date3/48
date4=date4/48
date5=date5/48
date=date1
date=(date1+date2+date3+date4+date5)/5

height1=np.array(height1)*marker
height1=height1[height1!=0]
height2=np.array(height2)*marker
height2=height2[height2!=0]
height3=np.array(height3)*marker
height3=height3[height3!=0]
height4=np.array(height4)*marker
height4=height4[height4!=0]
height5=np.array(height5)*marker
height5=height5[height5!=0]
height=height1
height=(height1+height2+height3+height4+height5)/5

acc1=np.array(acc1)*marker
acc1=acc1[acc1!=0]
acc2=np.array(acc2)*marker
acc2=acc2[acc2!=0]
acc3=np.array(acc3)*marker
acc3=acc3[acc3!=0]
acc4=np.array(acc4)*marker
acc4=acc4[acc4!=0]
acc5=np.array(acc5)*marker
acc5=acc5[acc5!=0]
acc=acc1
acc=(acc1+acc2+acc3+acc4+acc5)/5

fig=plt.figure(figsize=(20,15))
plt.scatter(dense,date,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0,np.max(dense)*1.05)
plt.ylim(143,148)
plt.xlabel('Population density(people/km^2)')
plt.ylabel('Peak-date(day)',fontsize=15)
plt.title('Population density & Peak-date',fontsize=15)
plt.show()

fig=plt.figure(figsize=(20,15))
plt.scatter(flow,date,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0.2,1.1)
plt.ylim(143,148)
plt.xlabel('Relatively flow',fontsize=15)
plt.ylabel('Peak-date(day)',fontsize=15)
plt.title('Population mobility & Peak-date',fontsize=15)
plt.show()

fig=plt.figure(figsize=(20,15))
plt.scatter(dense,height,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0,np.max(dense)*1.05)
plt.ylim(21,23)
plt.xlabel('Population density(people/km^2)',fontsize=15)
plt.ylabel('Peak-height(%)',fontsize=15)
plt.title('Population density & Peak-height',fontsize=15)
plt.show()

fig=plt.figure(figsize=(20,15))
plt.scatter(flow,height,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0.2,1.1)
plt.ylim(21,23)
plt.xlabel('Relatively flow',fontsize=15)
plt.ylabel('Peak-height(%)',fontsize=15)
plt.title('Population mobility & Peak-height',fontsize=15)
plt.show()

fig=plt.figure(figsize=(20,15))
plt.scatter(dense,acc,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0,np.max(dense)*1.05)
plt.ylim(90,95)
plt.xlabel('Population density(people/km^2)',fontsize=15)
plt.ylabel('Infect rate(%)',fontsize=15)
plt.title('Population density & Total infect rate after 1year',fontsize=15)
plt.show()

fig=plt.figure(figsize=(20,15))
plt.scatter(flow,acc,marker='o',color='red')
plt.grid()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0.2,1.1)
plt.ylim(90,95)
plt.xlabel('Relatively flow',fontsize=15)
plt.ylabel('Infect rate(%)',fontsize=15)
plt.title('Population mobility & Total infect rate after 1year',fontsize=15)
plt.show()

p=np.corrcoef([dense,flow,date,height,acc])
print(p)