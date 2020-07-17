import json
import matplotlib.pyplot as plt
import numpy as np
LIST=[0.9,0.8,0.7,0.6,1.0]
peak=[]
plt.figure(figsize=(6,4.64))
for II in range(len(LIST)):
    with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\result\\experiment9\\result-500d-{}β.json'.format(LIST[II]),'r') as f:
        result=json.load(f)
    N=np.sum(np.sum(result[0]))
    result=np.array(result)
    time=[]
    analyseI=[]
    analyseL=[]
    analyseR=[]
    analyseD=[]
    peaktime=0
    peaknum=0
    for i in range(np.shape(result)[0]):
        I=0
        L=0
        R=0
        D=0
        for j in range(np.shape(result)[1]):
            I+=result[i][j][2]
            I+=result[i][j][3]
            L+=result[i][j][1]
            R+=result[i][j][5]
            D+=result[i][j][6]
        analyseI.append(I)
        analyseL.append(L)
        analyseR.append(R)
        analyseD.append(D)
        time.append(i/48)
        if(peaknum<I):
            peaknum=I
            peaktime=i
    peak.append([peaktime,peaknum])
    if(LIST[II]==1.0):
        plt.plot(time,100*(analyseI/N),linestyle='-.',label='baseline',linewidth=2)
    else:
        plt.plot(time,100*(analyseI/N),label='$\gamma_0$'+'={}'.format(LIST[II]),linewidth=2)
    print('{}/{}'.format(II+1,len(LIST)))
plt.xlabel('t(day)',fontsize=15)
plt.ylabel('$r_I$(%)',fontsize=15)
plt.tick_params(labelsize=12)
plt.legend(fontsize=12)
plt.subplots_adjust(left=0.2,bottom=0.2)
plt.savefig('c:\\users\\郝千越\\desktop\\inblocks.png',dpi=100)
print(peak)
