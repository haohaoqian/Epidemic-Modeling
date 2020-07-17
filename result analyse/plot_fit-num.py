import json
import matplotlib.pyplot as plt
import numpy as np

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\result-365d-average-5.json','r') as f:
    data=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region.json','r') as f:
    pop=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\marker_region.json','r') as f:
    marker=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-num-5.json','r') as f:
    para=json.load(f)

def func(t,sigma,mu,m):
    return m*np.exp((-(t-mu)*(t-mu))/sigma)

num=np.zeros((len(data[0]),365*48))
date=np.zeros(365*48)
for t in range(365*48):
    for j in range(len(data[t])):
        if(marker[j]==0):
            continue
        if(sum(data[t][j])==0):
            num[j][t]=num[j][t-1]
        else:
            num[j][t]=(data[t][j][2]+data[t][j][3])/sum(data[t][j])
    date[t]=t/48

LIST=[101]
for j in LIST:
    fit=[]
    for i in range(int(para[j][0])):
        fit.append(func(i/48,para[j][1],para[j][2],para[j][3]))
    plt.figure(figsize=(6.4,4.76))
    plt.plot(date,num[j],label='raw',color='blue',linewidth=3)
    plt.plot(date[0:int(para[j][0])],fit,label='fit',color='red',linewidth=3)
    plt.xlabel('t(day)',fontsize=25)
    plt.ylabel('$r_I$(%)',fontsize=25)
    plt.tick_params(labelsize=20)
    plt.subplots_adjust(left=0.2,bottom=0.2)
    plt.legend(fontsize=25)
    plt.savefig('c:\\users\\郝千越\\desktop\\num-f.png',dpi=100)
    '''
    plt.figure(figsize=(6.4,4.76))
    plt.plot(date,num[j],label='raw',color='blue')
    plt.xlabel('t(day)',fontsize=15)
    plt.ylabel('$r_I$(%)',fontsize=15)
    plt.tick_params(labelsize=12)
    plt.savefig('c:\\users\\郝千越\\desktop\\num.png',dpi=100)
    '''
