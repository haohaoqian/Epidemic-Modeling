import json
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\dense_region.json','r') as f:
    dense=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\flow_region.json','r') as f:
    flow=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_date_region-1.json','r') as f:
    date=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_height_region-1.json','r') as f:
    height=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\acc_region-1.json','r') as f:
    acc=json.load(f)
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

dense=np.array(dense)
flow=np.array(flow)
date=np.array(date)
date2=np.array(date2)
date3=np.array(date3)
date4=np.array(date4)
date5=np.array(date5)
date=date/48
date2=date2/48
date3=date3/48
date4=date4/48
date5=date5/48
fig=plt.figure(figsize=(20,15))
plt.scatter(dense,date,c=date,marker='o',cmap=cm.Reds_r,vmin=140,vmax=152)
plt.scatter(dense,date2,c=date2,marker='o',cmap=cm.Reds_r,vmin=140,vmax=152)
plt.scatter(dense,date3,c=date3,marker='o',cmap=cm.Reds_r,vmin=140,vmax=152)
plt.scatter(dense,date4,c=date4,marker='o',cmap=cm.Reds_r,vmin=140,vmax=152)
plt.scatter(dense,date5,c=date5,marker='o',cmap=cm.Reds_r,vmin=140,vmax=152)
plt.grid()
plt.colorbar()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Population density(people/km^2)')
plt.ylabel('Peak-date(day)',fontsize=15)
plt.ylim(140,152)
plt.title('Population density & Peak-date',fontsize=15)
plt.show()
fig=plt.figure(figsize=(20,15))
plt.scatter(flow,date,c=date,marker='o',cmap=cm.Reds_r,vmin=140,vmax=152)
plt.scatter(flow,date2,c=date2,marker='o',cmap=cm.Reds_r,vmin=140,vmax=152)
plt.scatter(flow,date3,c=date3,marker='o',cmap=cm.Reds_r,vmin=140,vmax=152)
plt.scatter(flow,date4,c=date4,marker='o',cmap=cm.Reds_r,vmin=140,vmax=152)
plt.scatter(flow,date5,c=date5,marker='o',cmap=cm.Reds_r,vmin=140,vmax=152)
plt.grid()
plt.colorbar()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Relatively flow',fontsize=15)
plt.ylabel('Peak-date(day)',fontsize=15)
plt.ylim(140,152)
plt.title('Population mobility & Peak-date',fontsize=15)
plt.show()
fig=plt.figure(figsize=(20,15))
plt.scatter(dense,height,c=height,marker='o',cmap=cm.Reds,vmin=20,vmax=25)
plt.scatter(dense,height2,c=height2,marker='o',cmap=cm.Reds,vmin=20,vmax=25)
plt.scatter(dense,height3,c=height3,marker='o',cmap=cm.Reds,vmin=20,vmax=25)
plt.scatter(dense,height4,c=height4,marker='o',cmap=cm.Reds,vmin=20,vmax=25)
plt.scatter(dense,height5,c=height5,marker='o',cmap=cm.Reds,vmin=20,vmax=25)
plt.grid()
plt.colorbar()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Population density(people/km^2)',fontsize=15)
plt.ylabel('Peak-height(%)',fontsize=15)
plt.title('Population density & Peak-height',fontsize=15)
plt.ylim(20,25)
plt.show()
fig=plt.figure(figsize=(20,15))
plt.scatter(flow,height,c=height,marker='o',cmap=cm.Reds,vmin=20,vmax=25)
plt.scatter(flow,height2,c=height2,marker='o',cmap=cm.Reds,vmin=20,vmax=25)
plt.scatter(flow,height3,c=height3,marker='o',cmap=cm.Reds,vmin=20,vmax=25)
plt.scatter(flow,height4,c=height4,marker='o',cmap=cm.Reds,vmin=20,vmax=25)
plt.scatter(flow,height5,c=height5,marker='o',cmap=cm.Reds,vmin=20,vmax=25)
plt.grid()
plt.colorbar()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Relatively flow',fontsize=15)
plt.ylabel('Peak-height(%)',fontsize=15)
plt.title('Population mobility & Peak-height',fontsize=15)
plt.ylim(20,25)
plt.show()
fig=plt.figure(figsize=(20,15))
plt.scatter(dense,acc,c=acc,marker='o',cmap=cm.Reds,vmin=90,vmax=95)
plt.scatter(dense,acc2,c=acc2,marker='o',cmap=cm.Reds,vmin=90,vmax=95)
plt.scatter(dense,acc3,c=acc3,marker='o',cmap=cm.Reds,vmin=90,vmax=95)
plt.scatter(dense,acc4,c=acc4,marker='o',cmap=cm.Reds,vmin=90,vmax=95)
plt.scatter(dense,acc5,c=acc5,marker='o',cmap=cm.Reds,vmin=90,vmax=95)
plt.grid()
plt.colorbar()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Population density(people/km^2)',fontsize=15)
plt.ylabel('Infect rate(%)',fontsize=15)
plt.title('Population density & Total infect rate after 1year',fontsize=15)
plt.ylim(90,95)
plt.show()
fig=plt.figure(figsize=(20,15))
plt.scatter(flow,acc,c=acc,marker='o',cmap=cm.Reds,vmin=90,vmax=95)
plt.scatter(flow,acc2,c=acc2,marker='o',cmap=cm.Reds,vmin=90,vmax=95)
plt.scatter(flow,acc3,c=acc3,marker='o',cmap=cm.Reds,vmin=90,vmax=95)
plt.scatter(flow,acc4,c=acc4,marker='o',cmap=cm.Reds,vmin=90,vmax=95)
plt.scatter(flow,acc5,c=acc5,marker='o',cmap=cm.Reds,vmin=90,vmax=95)
plt.grid()
plt.colorbar()
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Relatively flow',fontsize=15)
plt.ylabel('Infect rate(%)',fontsize=15)
plt.title('Population mobility & Total infect rate after 1year',fontsize=15)
plt.ylim(90,95)
plt.show()