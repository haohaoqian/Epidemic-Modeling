import json
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import numpy as np
from matplotlib import colors

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\dense_region.json','r') as f:
    dense=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\flow_region.json','r') as f:
    flow=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_date_region.json','r') as f:
    date=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\peak_height_region.json','r') as f:
    height=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\acc_region.json','r') as f:
    acc=json.load(f)

dense=np.array(dense)
flow=np.array(flow)
date=np.array(date)
date=date/48
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(dense,flow,date,c=date,marker='o',cmap=cm.Reds_r,vmin=140,vmax=152)
ax.grid()
ax.set_xlabel('Population density(people/km^2)',fontsize=15)
ax.set_ylabel('Relatively flow',fontsize=15)
ax.set_zlabel('Peak-date(day)',fontsize=15)
ax.set_zlim(140,152)
ax.set_title('Peak-date',fontsize=15)
plt.show()
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(dense,flow,height,c=height,marker='o',cmap=cm.Reds,vmin=20,vmax=25)
ax.grid()
ax.set_xlabel('Population density(people/km^2)',fontsize=15)
ax.set_ylabel('Relatively flow',fontsize=15)
ax.set_zlabel('Peak-height(%)',fontsize=15)
ax.set_zlim(20,25)
ax.set_title('Peak-height',fontsize=15)
plt.show()
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(dense,flow,acc,c=acc,marker='o',cmap=cm.Reds,vmin=90,vmax=95)
ax.grid()
ax.set_xlabel('Population density(people/km^2)',fontsize=15)
ax.set_ylabel('Relatively flow',fontsize=15)
ax.set_zlabel('Infected-rate(%)',fontsize=15)
ax.set_zlim(90,95)
ax.set_title('Total infected rate after 1year',fontsize=15)
plt.show()