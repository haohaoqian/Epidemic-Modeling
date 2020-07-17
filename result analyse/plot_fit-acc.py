import json
import matplotlib.pyplot as plt
import numpy as np

with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\result-365d-average-5.json','r') as f:
    data=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_region.json','r') as f:
    pop=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\marker_region.json','r') as f:
    marker=json.load(f)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment7\\不同区域发展速度\\para-acc-5.json','r') as f:
    para=json.load(f)

def func(t,a,m):
    return m*(np.exp(a*t)-1)+0.1

acc=np.zeros((len(data[0]),365*48))
date=np.zeros(365*48)
for t in range(365*48):
    for j in range(len(data[t])):
        if(marker[j]==0):
            continue
        if(sum(data[t][j])==0):
            acc[j][t]=acc[j][t-1]
        else:
            acc[j][t]=(sum(data[t][j])-data[t][j][0])/sum(data[t][j])
    date[t]=t/48

LIST=[101]
for j in LIST:
    fit=list()
    for i in range(int(para[j][1])-int(para[j][0])+960):
        fit.append(func((i-480)/48,para[j][2],para[j][3]))
    plt.figure(figsize=(6.4,4.76))
    plt.plot(date,acc[j],label='raw',color='blue',linewidth=3)
    plt.plot(date[int(para[j][0])-480:int(para[j][1])+480],fit,label='fit',color='red',linewidth=3)
    plt.xlabel('t(day)',fontsize=25)
    plt.ylabel('$r_{aI}$(%)',fontsize=25)
    plt.tick_params(labelsize=20)
    plt.ylim(-0.05,1.05)
    plt.subplots_adjust(left=0.2,bottom=0.2)
    plt.legend(fontsize=25)
    plt.savefig('c:\\users\\郝千越\\desktop\\acc-f.png',dpi=100)
    '''
    plt.figure(figsize=(6.4,4.76))
    plt.plot(date,acc[j],label='raw',color='blue')
    plt.xlabel('t(day)',fontsize=25)
    plt.ylabel('$r_{aI}$(%)',fontsize=25)
    plt.tick_params(labelsize=20)
    plt.ylim(-0.05,1.05)
    plt.savefig('c:\\users\\郝千越\\desktop\\acc.png',dpi=100)
    '''