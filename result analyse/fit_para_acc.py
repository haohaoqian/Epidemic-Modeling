import json
import numpy as np
from scipy.optimize import curve_fit

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment8\\不同区域发展速度\\result-365d-average-5.json','r') as f:
    data=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region_marker.json','r') as f:
    marker=json.load(f)

def func(t,a,m):
    return m*(np.exp(a*t)-1)+0.1

acc=np.zeros((len(data[0]),365*48))
date=np.zeros(365*48)
start=np.zeros(len(data[0]))
end=np.zeros(len(data[0]))
for t in range(365*48):
    for j in range(len(data[t])):
        if(marker[j]==0):
            continue
        if(sum(data[t][j])==0):
            acc[j][t]=acc[j][t-1]
        else:
            acc[j][t]=(sum(data[t][j])-data[t][j][0])/sum(data[t][j])
        if(start[j]==0 and acc[j][t]>=0.1):
            start[j]=t
        if(end[j]==0 and acc[j][t]>=0.7):
            end[j]=t
    date[t]=t/48

for i in range(len(data[t])):
    if(marker[i]!=0 and end[i]==0):
        end[i]=365*48
    if(start[i]<5000):
        marker[i]=0
para=list()
for i in range(675):
    if(marker[i]==0):
        para.append([0,0,0,0,0])
        continue
    popt, pcov = curve_fit(func, date[0:int(end[i])-int(start[i])], acc[i][int(start[i]):int(end[i])],maxfev=100000,bounds=([0,0],[0.1,np.inf]))
    fit=np.zeros(int(end[i])-int(start[i]))
    for j in range(int(end[i])-int(start[i])):
        fit[j]=(func(j/48,popt[0],popt[1]))
    ybar = np.sum(acc[i][int(start[i]):int(end[i])]) / (int(end[i])-int(start[i]))
    ssreg = np.sum((fit -acc[i][int(start[i]):int(end[i])])**2)
    sstot = np.sum((acc[i][int(start[i]):int(end[i])] - ybar)**2)
    r=(1-ssreg / sstot)**0.5
    para.append([start[i],end[i],popt[0],popt[1],r])
    print('{}/675'.format(i+1))

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-acc-5.json','w') as f:
    json.dump(para,f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region_marker.json','w') as f:
    json.dump(marker,f)