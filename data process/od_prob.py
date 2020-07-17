import json
import numpy as np

od=np.zeros((1488,675,675),dtype=np.int)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\raw\\od_region_30','r') as f:
    for line in f:
        tim_loc,pop=line.strip("\r\n").split("\t")
        time,loco,locd=tim_loc.split('=')
        loco=loco.replace('0-','',1)
        locd=locd.replace('0-','',1)
        time=int(time)
        pop=int(pop)
        loco=int(loco)
        locd=int(locd)
        od[time][loco][locd]=pop
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\pop_record.json','r') as f:
    pop_record=json.load(f)
od_prob=np.zeros((7*48,675,676),dtype=np.float)
for i in range(336,1344):
    for o in range(675):
        for d in range(675):
            if(pop_record[i-1][o]!=0):
                od_prob[(i-336)%(7*48)][o][d]+=od[i][o][d]/pop_record[i-1][o]
            else:
                od_prob[(i-336)%(7*48)][o][d]+=1/675
od_prob=od_prob/3
#处理舍入误差导致的和大于1
s=np.sum(od_prob,axis=2)
for i in range(336):
    for j in range(675):
        if(s[i][j]>1):
            t=np.argmax(od_prob[i][j])
            od_prob[i][j][t]-=(s[i][j]-0.999999999)
with open('D:\\郝千越文件\\其他\\SRT\\疫情传播建模\\data_beijing_region\\processed\\od_prob.json','w') as f:
    json.dump(od_prob.tolist(),f)