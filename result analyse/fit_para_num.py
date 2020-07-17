import json
import numpy as np
from scipy.optimize import curve_fit

for x in range(1,6):

    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\result-365d-average-{}.json'.format(x),'r') as f:
        data=json.load(f)
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region.json','r') as f:
        pop=json.load(f)
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region_marker.json','r') as f:
        marker=json.load(f)

    def func(t,sigma,mu,m):
        return m*np.exp((-(t-mu)*(t-mu))/sigma)

    num=np.zeros((len(data[0]),365*48))
    date=np.zeros(365*48)
    end=np.zeros(len(data[0]))
    for t in range(365*48):
        for j in range(len(data[t])):
            if(marker[j]==0):
                continue
            if(sum(data[t][j])==0):
                num[j][t]=num[j][t-1]
            else:
                num[j][t]=(data[t][j][2]+data[t][j][3])/sum(data[t][j])
            if(end[j]==0 and num[j][t]>=0.17):
                end[j]=-1
            if(end[j]==-1 and num[j][t]<=0.15):
                end[j]=t
        date[t]=t/48

    for i in range(len(data[t])):
        if(marker[i]!=0 and (end[i]==0 or end[i]==-1)):
            end[i]=365*48
        if(end[i]<7000):
            marker[i]=0

    para=list()
    for i in range(675):
        if(marker[i]==0):
            para.append([0,0,0,0,0])
            continue
        popt, pcov = curve_fit(func, date[0:int(end[i])], num[i][0:int(end[i])],maxfev=100000,bounds=([0,100,0.1],[np.inf,200,0.3]))
        fit=np.zeros(int(end[i]))
        for j in range(int(end[i])):
            fit[j]=(func(j/48,popt[0],popt[1],popt[2]))
        ybar = np.sum(num[i][0:int(end[i])]) / int(end[i])
        ssreg = np.sum((fit -num[i][0:int(end[i])])**2)
        sstot = np.sum((num[i][0:int(end[i])] - ybar)**2)
        r=(1-ssreg / sstot)**0.5
        para.append([end[i],popt[0],popt[1],popt[2],r])
        print('{}/675'.format(i+1))

    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-num-{}.json'.format(x),'w') as f:
        json.dump(para,f)
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region_marker.json','w') as f:
        json.dump(marker,f)